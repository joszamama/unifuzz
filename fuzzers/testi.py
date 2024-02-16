# Implement your grammar here in the `grammar` variable.
# You may define additional functions, e.g. for generators.
# You may not import any other modules written by yourself.
# That is, your entire implementation must be in `grammar.py`
# and `fuzzer.py`.

import random
from typing import Set, Union
from fuzzingbook.GeneratorGrammarFuzzer import opts

table_names: Set[str] = set()

def define_table(id: str) -> None:
    table_names.add(id)

def use_table() -> Union[None, str]:
    if len(table_names) == 0:
        return None

    id = random.choice(list(table_names))
    return id

grammar = {
    "<start>": ["<sqlite_statements>"],
    "<sqlite_statements>": ["<create_table>", "<create_index>", "<create_trigger>", "<create_view>", "<create_virtual_table>", 
                            "<alter_table>", "<analyze_stmt>", "<attach_database>", "<detach_database>", "<select_stmt>", "<delete_stmt>", 
                            "<drop_index>", "<drop_table>", "<drop_trigger>", "<drop_view>","<explain_clause>", "<insert_stmt>", 
                            "<pragma_stmt>", "<reindex_stmt>", "<release_stmt>", "<replace_stmt>", "<returning_clause>", "<begin_transaction>", "<commit_transaction>", "<rollback_transaction>", 
                            "<create_savepoint>", "<update_stmt>", "<upsert_stmt>", "<vacuum_stmt>", "<value_clause>", "<with_clause>", "<release_stmt>"],

    "<create_table>": [("CREATE TABLE <table_name> (<table_columns>)", opts(post=lambda id, col: define_table(id))),
        ("CREATE TABLE <table_name> (<table_columns>)", opts(post=lambda id, col: define_table(id))),
        ("CREATE TEMPORARY TABLE IF NOT EXISTS <table_name> (<table_columns>) WITHOUT ROWID", opts(post=lambda id, col: define_table(id))),
        ("CREATE TABLE <table_name> (<table_columns>) INDEXED BY <index_name>", opts(post=lambda id, col, tb: define_table(id))),
        ("CREATE TABLE <table_name> AS <select_stmt>", opts(post=lambda id, col: define_table(id)))],

    "<explain_clause>": ["EXPLAIN QUERY PLAN <select_stmt>", "EXPLAIN <select_stmt>"],

    "<select_stmt>": [
        ("SELECT <select_type> <select_columns> FROM <table_name> <join_clause> WHERE <condition_stmt>", opts(post=lambda col, id, cla, con, se: [None, None, use_table(),None, None])),
        ("SELECT <select_type> <select_columns> FROM <table_name> WHERE <condition_stmt>", opts(post=lambda col, id, con, se: [None, None, use_table(),None])),
        ("SELECT <select_type> <select_columns> FROM <table_name>", opts(post=lambda col, id, se: [None, None, use_table()])),
        ("SELECT <select_type> <select_columns> FROM <table_name> <join_clause> WHERE <condition_stmt> GROUP BY <group_by_columns> HAVING <condition_stmt> ORDER BY <order_by_columns> LIMIT <int_string>", opts(post=lambda col, id, cla, con, bol, dol, hol, eol, se: [None, None, use_table(),None, None, None,None,None,None])),
        ("SELECT <select_type> <select_columns> FROM <table_name> WHERE <condition_stmt> GROUP BY <group_by_columns> HAVING <condition_stmt> ORDER BY <order_by_columns> LIMIT <int_string>", opts(post=lambda col, id, cla, con, bol, dol, hol, se: [None, None, use_table(),None, None, None,None,None])),
        ("SELECT <select_type> <select_columns> FROM <table_name> ORDER BY <order_by_columns> LIMIT <int_string>", opts(post=lambda col, id, cla, con, se: [None, None, use_table(),None, None])),
        ("SELECT <select_type> <select_columns> FROM <table_name> <indexed_by_clause> WHERE <condition_stmt>", opts(post=lambda col, id, cla, con, se: [None, None, use_table(),None, None])),
        ("SELECT <select_type> <select_columns> FROM <table_name> <indexed_by_clause>", opts(post=lambda col, idx, id, se: [None, None, use_table(), None])),
        "<select_stmt> UNION <select_stmt>",
        "<select_stmt> UNION ALL <select_stmt>",
        "<select_stmt> INTERSECT <select_stmt>",
        "<select_stmt> EXCEPT <select_stmt>",],
    
    "<star>": ["*"],

    "<select_type>": ["","DISTINCT","ALL"],
    "<alter_table>": [("ALTER TABLE <table_name> <alter_action>", opts(post=lambda id, con: [use_table(),None]))],
    "<alter_action>": ["ADD COLUMN <table_column_type>",
                        "RENAME TO <charstring>",
                        "RENAME COLUMN <charstring> TO <charstring>",
                        "ALTER COLUMN <charstring> TYPE <column_data_type>",
                        "MODIFY COLUMN <charstring> <column_data_type>",
                        "ADD CONSTRAINT <charstring> <check_clause>",
                        "DROP CONSTRAINT <charstring>",
                        "DISABLE TRIGGER <charstring>",
                        "ENABLE TRIGGER <charstring>",
                        "RENAME TO <charstring>",
                        "ALTER COLUMN <charstring> TYPE <column_data_type>",
                        "MODIFY COLUMN <charstring> <column_data_type> <constraint_type>",
                        "DROP CONSTRAINT IF EXISTS <charstring> CASCADE"],

    "<constraint_type>": [  "<check_clause>",
                            "NOT NULL <conflict_clause>",
                            "UNIQUE <conflict_clause>",
                            "PRIMARY KEY (<column_list>)",
                            "PRIMARY KEY <conflict_clause>",
                            "DEFAULT (<expr_stmt>)",
                            "COLLATE <charstring>",
                            ("FOREIGN KEY (<column_name>) REFERENCES <table_name> (<column_name>)", opts(post=lambda col, id, cla: [None, use_table(),None])),
                            "UNIQUE (<column_list>)",
                            "UNIQUE (<column_list>) WHERE <condition_stmt>",
                            "GENERATZED ALWAYS AS (<expr_stmt>)",
                            "GENERATZED ALWAYS AS (<expr_stmt>) STORED",
                            "GENERATZED ALWAYS AS (<expr_stmt>) VIRTUAL"],

    "<conflict_clause>": ["ON CONFLICT <conflict_type>"],
    "<conflict_type>": ["ROLLBACK", "ABORT", "FAIL", "IGNORE", "REPLACE"],
    
    "<check_clause>": [
        "CHECK (<expr_stmt>)",
        "CHECK <condition_stmt>"
    ],
    "<analyze_stmt>": [("ANALYZE <table_name>", opts(post=lambda id: [use_table()]))],
    "<attach_database>": ["ATTACH DATABASE <charstring> AS <charstring>"],
    "<detach_database>": ["DETACH DATABASE <charstring>", "DETACH DATABASE <charstring> CASCADE"],
    
    
    "<begin_transaction>": ["BEGIN TRANSACTION", "BEGIN <begin_type> TRANSACTION"],
    "<begin_type>": ["DEFERRED", "IMMEDIATE", "EXCLUSIVE"],
    "<commit_transaction>": ["COMMIT TRANSACTION", "END TRANSACTION", "COMMIT", "END"],
    "<rollback_transaction>": ["ROLLBACK TRANSACTION", "ROLLBACK", "ROLLBACK TO <savepoint_name>", "ROLLBACK TO SAVEPOINT <savepoint_name>"],
    
    "<create_index>": [
        ("CREATE INDEX <index_name> ON <table_name> (<index_column>)", opts(post=lambda col, id, cla: [None, use_table(),None])),
        ("CREATE UNIQUE INDEX <index_name> ON <table_name> (<index_column>) WHERE <condition_stmt>", opts(post=lambda col, id, cla, con: [None, use_table(),None, None]))
    ],
    "<index_name>": ["<charstring>"],
    "<create_trigger>": [("CREATE TRIGGER <charstring> <trigger_event> ON <table_name> <trigger_action>", opts(post=lambda col, id, cla, con: [None, None, use_table(), None]))],
    "<trigger_event>": ["BEFORE INSERT", "AFTER INSERT", "BEFORE UPDATE", "AFTER UPDATE", "BEFORE DELETE", "AFTER DELETE"],
    "<trigger_action>": ["BEGIN <insert_stmt> END", "BEGIN <delete_stmt> END", "BEGIN <update_stmt> END", "BEGIN <select_stmt> END"],

    "<create_view>": ["CREATE VIEW <view_name> AS <select_stmt>",
                      "CREATE VIEW IF NOT EXISTS <view_name> AS <select_stmt>"
                      "CREATE VIEW <view_name> (<column_list>) AS <select_stmt>",
                      "CREATE VIEW IF NOT EXISTS <view_name> (<column_list>) AS <select_stmt>"],
                      
    "<create_virtual_table>": [("CREATE VIRTUAL TABLE <table_name> USING <module_name> (<module_args>)", opts(post=lambda id, col, tb: define_table(id)))],

    "<delete_stmt>": [("DELETE FROM <table_name>", opts(post=lambda id: [use_table()])),
                 ("DELETE FROM <table_name> WHERE <condition_stmt>", opts(post=lambda col, id: [use_table(), None])),
                 ("DELETE FROM <table_name> WHERE <condition_stmt> (<select_stmt>)", opts(post=lambda col, id, cla: [use_table(),None, None])),
                 ("DELETE FROM <table_name> <indexed_by_clause> WHERE <condition_stmt> (<select_stmt>)", opts(post=lambda col, id, tb, cla: [use_table(),None, None, None]))
                 ],
    
    "<drop_index>": ["DROP INDEX <charstring>", "DROP INDEX IF EXISTS <charstring>"],
    "<drop_table>": [("DROP TABLE <table_name>", opts(post=lambda id: [use_table()])), 
                     ("DROP TABLE IF EXISTS <table_name>", opts(post=lambda id: [use_table()]))],
    "<drop_trigger>": ["DROP TRIGGER <charstring>", "DROP TRIGGER IF EXISTS <charstring>"],
    "<drop_view>": ["DROP VIEW <view_name>", "DROP VIEW IF EXISTS <view_name>"],
    
    
    "<expr_stmt>": ["<math_expr>", "<constant_value>", "<datetime_func>", "<case_expr>", "<subquery>", "<raise_func>"],
    "<math_expr>": ["<expr_stmt> + <expr_stmt>", "<expr_stmt> - <expr_stmt>", "<expr_stmt> * <expr_stmt>", "<expr_stmt> / <expr_stmt>"],
    "<case_expr>": ["CASE WHEN <condition_stmt> THEN <expr_stmt> ELSE <expr_stmt> END"],
    "<subquery>": ["(<select_stmt>)"],
    
    "<raise_func>": ["RAISE (ROLLBACK, <charstring>)",
                         "RAISE (ABORT, <charstring>)",
                         "RAISE (FAIL, <charstring>)", 
                         "<raise_ignore>"],
    "<raise_ignore>":["RAISE (IGNORE)"],

    "<datetime_func>": ["<datetime_func_name> (<function_args>)"],
    "<datetime_func_name>": ["DATE", "TIME", "DATETIME", "STRFTIME", "JULIANDAY", "UNIXEPOCH", "TIMEDIFF"],
    "<function_args>": ["<datetime_expr>", "<datetime_expr>,<datetime_modifier>"],
    "<datetime_expr>":["CURRENT_DATE", "CURRENT_TIME", "CURRENT_TIMESTAMP", "now", "<int_string>"],
    "<datetime_modifier>": ["days", "hours", "minutes", "seconds", "months", "years", "start of month", "start of year", "start of day", "unixepoch", "julianday", "auto",
                             "localtime", "utc", "subsec", "subsecond"],

    "<indexed_by_clause>": ["INDEXED BY <index_name>"],
    
    "<insert_stmt>": [("INSERT INTO <table_name> (<insert_columns>) VALUES (<insert_values>)", opts(post=lambda col, id, cla: [use_table(),None, None])), 
                 ("INSERT INTO <table_name> DEFAULT VALUES", opts(post=lambda id: [use_table()])), 
                 ("INSERT INTO <table_name> (<insert_columns>) VALUES (<insert_values>) ON CONFLICT (<conflict_columns>) DO UPDATE SET <update_action> WHERE <condition_stmt> RETURNING <select_columns>", opts(post=lambda col, id, cla, con, bol, dol, hol: [use_table(),None, None, None,None,None,None])),
                 ("INSERT INTO <table_name> DEFAULT VALUES ON CONFLICT (<conflict_columns>) DO NOTHING RETURNING <select_columns>", opts(post=lambda col, id, cla: [use_table(),None, None]))],
    
    "<insert_columns>": ["<column_name>", "<insert_columns>,<column_name>"],
    "<default_value>": ["<expr_stmt>", "NULL", "CURRENT_DATE", "CURRENT_TIME", "CURRENT_TIMESTAMP"],
    "<group_by_columns>": ["<column_name>", "<expr_stmt>", "<group_by_columns>, <column_name>"],
    "<order_by_columns>": ["<column_name> <collate> ASC <nulls>", "<column_name> <collate> DESC <nulls>", "<expr_stmt> <collate> ASC <nulls>", "<expr_stmt> <collate> DESC <nulls>"],
    "<collate>":["", "COLLATE <charstring>"],
    "<nulls>":["", "NULLS FIRST", "NULLS LAST"],
    "<insert_values>": ["<expr_stmt>", "<insert_values>,<expr_stmt>"],
    
    "<pragma_stmt>": ["PRAGMA <pragma_func>",
                "PRAGMA <pragma_func> (<expr_stmt>)",
                ("PRAGMA foreign_key_check(<table_name>)", opts(post=lambda id: [use_table()])),
                ("PRAGMA foreign_key_list(<table_name>)", opts(post=lambda id: [use_table()])),
                ("PRAGMA index_list(<table_name>)", opts(post=lambda id: [use_table()])),
                ("PRAGMA table_info(<table_name>)", opts(post=lambda id: [use_table()])),
                ("PRAGMA freelist_count(<table_name>)", opts(post=lambda id: [use_table()])),
                ("PRAGMA table_info(<table_name>)", opts(post=lambda id: [use_table()])),
                ("PRAGMA table_list(<table_name>)", opts(post=lambda id: [use_table()])),
                ("PRAGMA table_xinfo(<table_name>)", opts(post=lambda id: [use_table()])),
                "PRAGMA index_info(<index_name>)",
                ],
    "<pragma_func>": ["cache_size", "collation_list", "database_list", "encoding", "foreign_keys", "foreign_key_check" "synchronous", "journal_mode", "temp_store", "fullfsync", "table_list", "locking_mode",
                       "page_count", "page_size", "recursive_triggers", "schema_version", "secure_delete", "soft_heap_limit", "user_version", "wal_autocheckpoint",
                         "wal_checkpoint", "writable_schema"],

    "<reindex_stmt>": ["REINDEX", "REINDEX <charstring>", "REINDEX COLLATION <charstring>"],
    "<release_stmt>": ["RELEASE SAVEPOINT <charstring>", "RELEASE <savepoint_name>", "RELEASE <savepoint_name> ON CONFLICT IGNORE"],
    "<replace_stmt>": [("REPLACE INTO <table_name> (<insert_columns>) VALUES (<insert_values>)", opts(post=lambda col, id, cla: [use_table(),None, None]))],
    "<returning_clause>": ["RETURNING <select_columns>", "RETURNING *"],
    "<select_columns>": ["<column_name>", "<star>", "<aggregate_func_stmt>", "<column_name>,<select_columns>", "<window_func_stmt>"],
    "<aggregate_func_stmt>": ["<aggregate_func_name> (<column_name>)", "<aggregate_func_name> (<expr_stmt>)"],
    "<aggregate_func_name>": ["SUM", "AVG", "COUNT", "MAX", "MIN", "TOTAL"],
    "<column_list>": ["<column_name>", "<column_name> <column_list>"],
    
    "<create_savepoint>": ["SAVEPOINT <savepoint_name>", "SAVEPOINT <savepoint_name> ON CONFLICT ROLLBACK", "SAVEPOINT <savepoint_name> ON CONFLICT ABORT"],
    "<savepoint_name>": ["<charstring>"],
    
    "<release_stmt>": ["RELEASE SAVEPOINT <charstring>", "RELEASE <savepoint_name>", "RELEASE <savepoint_name> ON CONFLICT IGNORE"],

    "<join_clause>": [("<join_type> JOIN <table_name> ON <join_condition>", opts(post=lambda col, id, cla: [None,use_table(),None])),
                      ("<join_type> JOIN <table_name> USING (<column_list>))", opts(post=lambda col, id, cla: [None,use_table(),None]))],
    "<join_type>": ["INNER", "LEFT", "RIGHT", "FULL"],
    "<join_condition>": ["<column_name> = <column_name>", "<expr_stmt> <comparison_symbol> <expr_stmt>"],
    
    "<update_stmt>": [("UPDATE <table_name> SET <update_action> WHERE <condition_stmt>", opts(post=lambda col, id, cla: [use_table(),None, None])),
                 ("UPDATE <table_name> SET <update_action> WHERE <condition_stmt> (<select_stmt>)", opts(post=lambda col, id, cla, con: [use_table(),None,None, None])),
                 ("UPDATE <table_name> SET <update_action> WHERE <condition_stmt> <indexed_by_clause>", opts(post=lambda col, id, tb, cla: [use_table(),None, None, None]))
                 ],
    "<update_action>": ["<column_name> = <expr_stmt>",
                        "<update_action>,<column_name> = <expr_stmt>",
                        "<column_name> = <expr_stmt> DEFAULT <default_value>",
                        "<update_action>,<column_name> = <expr_stmt> DEFAULT <default_value>"],
    "<upsert_stmt>": [
        ("INSERT INTO <table_name> (<insert_columns>) VALUES (<insert_values>) ON CONFLICT (<conflict_columns>) DO UPDATE SET <update_action> WHERE <condition_stmt>", opts(post=lambda col, id, cla, con, bol, dol: [use_table(),None, None,None,None,None])),
        ("INSERT INTO <table_name> (<insert_columns>) VALUES (<insert_values>) ON CONFLICT (<conflict_columns>) DO NOTHING", opts(post=lambda col, id, cla, con: [use_table(),None,None, None]))
    ],
    "<conflict_columns>": ["<column_name>", "<conflict_columns>,<column_name>"],
    "<vacuum_stmt>": ["VACUUM", "VACUUM INTO <charstring>"],
    
    "<value_clause>":["VALUES (<expr_stmt>)"],

    "<with_clause>": ["WITH <with_table_expr>", "WITH RECURSIVE <with_table_expr>"],
    "<with_table_expr>": [
        "<table_expr>", "<with_table_expr>, <table_expr>"
    ],
    
    "<table_expr>": [("<table_name> AS (<select_stmt>)", opts(post=lambda col, id: [use_table(), None])),
                                  ("<table_name> (<column_list>) AS NOT MATERIALIZED (<select_stmt>)", opts(post=lambda col, tb, id: [use_table(), None, None])),
                                  ("<table_name> (<column_list>) AS MATERIALIZED (<select_stmt>)", opts(post=lambda col, tb, id: [use_table(), None, None])),
                                  ("<table_name> (<column_list>) AS (<select_stmt>)", opts(post=lambda col, tb, id: [use_table(), None, None]))],
    "<table_name>": ["<charstring>"],
    
    "<table_columns>": ["<table_column_type>", "<table_columns>,<table_column_type>"],
    "<table_column_type>": ["<column_name> <column_data_type>", "<column_name> <column_data_type> <constraint_type>", "<column_name> <constraint_type>"],

    "<window_func_stmt>": ["<window_func> (<window_expr>) OVER <charstring>"],
    "<window_func>": ["<aggregate_func_name>", "<window_func_name>"],
    "<window_func_name>": ["ROW_NUMBER", "RANK", "DENSE_RANK","PERCENT_RANK","CUME_DIST", "NTILE", "LEAD", "LAG", "FIRST_VALUE", "LAST_VALUE", "NTH_VALUE"],
    "<window_expr>":["<star>", "<expr_stmt>",""],

    "<column_data_type>": ["TEXT", "INTEGER", "REAL", "BLOB", "NUMERIC", "BOOLEAN"],
    "<view_name>": ["<charstring>"],
    "<module_args>": ["<expr_stmt>", "<module_args>,<expr_stmt>"],
    "<module_name>": ["<charstring>"],
    "<index_column>": ["<column_name>", "<index_column>,<column_name>"],
    "<column_name>": ["<charstring>"],
    "<condition_stmt>": [
        "<expr_stmt> <comparison_symbol> <expr_stmt>",
        "NOT <expr_stmt> <comparison_symbol> <expr_stmt>",
        "EXISTS (<select_stmt>)",
        "NOT EXISTS (<select_stmt>)",
        "<expr_stmt> IN (<select_stmt>)",
        "<expr_stmt> NOT IN (<select_stmt>)"
        "<condition_stmt> AND <condition_stmt>",
        "<expr_stmt> BETWEEN <expr_stmt> AND <expr_stmt>",
        "<expr_stmt> NOT BETWEEN <expr_stmt> AND <expr_stmt>",
        "<condition_stmt> OR <condition_stmt>",
        "(<condition_stmt>)"
    ],
    "<comparison_symbol>": [
        "=", "<greater_symbol>", "<greater_symbol>=", "<less_symbol>", ">=", "!=", "<less_symbol><greater_symbol>", "LIKE","GLOB","REGEXP","MATCH", "BETWEEN", "IS NULL", "IS NOT NULL"
    ],

    "<greater_symbol>": [">"],
    "<less_symbol>": ["<"],
    
    "<constant_value>": ["<int_string>", "<charstring>", "<boolean_value>", "<null>"],

    "<null>":["NULL"],
    "<boolean_value>": ["TRUE", "FALSE"],
    
    "<int_string>": ["<digit>", "<digit><int_string>"],
    "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],

    "<charstring>": ["<character>", "<character><charstring>"],
    "<character>": [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y","Z"]
}