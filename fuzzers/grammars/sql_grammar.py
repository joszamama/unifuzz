SQL_GRAMMAR = {
    "<start>": [
                "<explain_statement_>"
                ],

    "<create_table_>": ["CREATE <temp_temporary_> TABLE <if_not_exists_> <schema_table_name_> <create_table_sub_>;"],
    "<create_table_sub_>": ["AS <select_statement_>", "(<column_defs_>)", "(<column_defs_>) <table_options_>",
                            "(<column_defs_> <table_constraints_>)", "(<column_defs_> <table_constraints_>) <table_options_>"],

    "<drop_table_>": ["DROP TABLE <if_exists_> <schema_table_name_>;"],

    "<alter_table_>": ["ALTER TABLE <schema_table_name_> <alter_table_sub_>;"],

    "<alter_table_sub_>": ["RENAME TO <table_name_>", "RENAME <alter_table_sub_2_> <string_> TO <string_>", "ADD <alter_table_sub_2_> <column_def_>", "DROP <alter_table_sub_2_> <string_>"],

    "<alter_table_sub_2_>": ["COLUMN", ""],


    "<insert_statement_>": [
        "<statement_start_with_> REPLACE INTO <schema_table_name_> <insert_statement_sub_> <insert_statement_sub_2_> <insert_statement_choices_> <return_clauses_>;",
        "<statement_start_with_> INSERT <update_insert_or> INTO <schema_table_name_> <insert_statement_sub_> <insert_statement_sub_2_> <insert_statement_choices_> <return_clauses_>;"],
    "<insert_statement_choices_>": ["<insert_statement_sub_3_>", "<insert_statement_sub_4_>",
                                    "<insert_statement_sub_5_>"],
    "<insert_statement_sub_>": ["AS <string_>", ""],
    "<insert_statement_sub_2_>": ["(<column_name_>)", ""],
    "<insert_statement_sub_3_>": ["VALUES <exprs_> <insert_statement_sub_6_>",
                                  "VALUES <exprs_paranthesis_> <insert_statement_sub_6_>"],
    "<insert_statement_sub_4_>": ["<select_statement_> <insert_statement_sub_6_>"],
    "<insert_statement_sub_5_>": ["DEFAULT VALUES"],
    "<insert_statement_sub_6_>": ["<upsert_clause_>", ""],

    "<upsert_clause_>": ["<upsert_clause_sub_1_>", "<upsert_clause_sub_1_> <upsert_clause_>"],
    "<upsert_clause_sub_1_>": ["ON CONFLICT <upsert_clause_sub_> DO <upsert_clause_sub_2_>"],
    "<upsert_clause_sub_>": ["(<indexed_columns_>)", "(<indexed_columns_>) WHERE <expr_>", ""],
    "<upsert_clause_sub_2_>": ["NOTHING", "UPDATE SET <upsert_clause_sub_2_1_>", "UPDATE SET <upsert_clause_sub_2_1_> WHERE <expr_>"],
    "<upsert_clause_sub_2_1_>": ["<column_name_>=<expr_>", "(<column_name_>)=<expr_>",
                                 "<column_name_>=<expr_>,<upsert_clause_sub_2_1_>", "(<column_name_>)=<expr_>,<upsert_clause_sub_2_1_>"],

    "<column_defs_>": ["<column_def_>", "<column_def_>,<column_defs_>"],
    "<column_def_>": ["<string_>", "<string_> <type_name_>",
                      "<string_> <type_name_> <column_constraint_>", "<string_> <column_constraint_>"],

    "<type_name_>": ["<string_>", "<string_> (<type_name_signed_number_>)"],
    "<type_name_signed_number_>": ["<signed_number_>", "<signed_number_>,<signed_number_>", ""],

    "<column_constraint_>": ["<column_constraint_sub_> <column_constraint_choices_>"],
    "<column_constraint_choices_>": ["<column_constraint_sub_2_>", "<column_constraint_sub_3_>",
                                     "<column_constraint_sub_4_>",
                                     "<column_constraint_sub_5_>", "<column_constraint_sub_6_>",
                                     "<column_constraint_sub_7_>",
                                     "<column_constraint_sub_8_>", "<column_constraint_sub_9_>"],
    "<column_constraint_sub_>": ["CONSTRAINT <string_>", ""],
    "<column_constraint_sub_2_>": ["PRIMARY KEY <asc_desc_> <conflict_clause_> <column_constraint_sub_2_1_>"],
    "<column_constraint_sub_2_1_>": ["AUTOINCREMENT", ""],
    "<column_constraint_sub_3_>": ["NOT NULL <conflict_clause_>"],
    "<column_constraint_sub_4_>": ["UNIQUE <conflict_clause_>"],
    "<column_constraint_sub_5_>": ["CHECK (<expr_>)"],
    "<column_constraint_sub_6_>": ["DEFAULT (<expr_>)", "DEFAULT <literal_value_>", "DEFAULT <signed_number_>"],
    "<column_constraint_sub_7_>": ["COLLATE <string_>"],
    "<column_constraint_sub_8_>": ["<foreign_key_clause_>"],
    "<column_constraint_sub_9_>": ["<column_constraint_sub_10_> AS (<expr_>) <column_constraint_sub_11_>"],
    "<column_constraint_sub_10_>": ["GENERATED ALWAYS", ""],
    "<column_constraint_sub_11_>": ["STORED", "VIRTUAL", ""],

    "<table_constraints_>": ["<table_constraint_>", "<table_constraint_>,<table_constraints_>"],
    "<table_constraint_>": ["<table_constraint_sub_> <table_constraint_sub_2_>"],
    "<table_constraint_sub_>": ["CONSTRAINT <string_>", ""],
    "<table_constraint_sub_2_>": ["PRIMARY KEY (<indexed_columns_> <conflict_clause_>)",
                                  "UNIQUE (<indexed_columns_> <conflict_clause_>)",
                                  "CHECK (<expr_>)", "FOREIGN KEY (<column_name_>) <foreign_key_clause_>"],

    "<foreign_key_clause_>": [
        "REFERENCES <table_name_> <foreign_key_clause_sub_> <foreign_key_clause_sub_2_> <foreign_key_clause_sub_3_> <foreign_key_clause_sub_4_>"],
    "<foreign_key_clause_sub_>": ["(<column_name_>)", ""],
    "<foreign_key_clause_sub_2_>": ["ON <foreign_key_clause_sub_2_1_> <foreign_key_clause_sub_2_2_>",
                                    "ON <foreign_key_clause_sub_2_1_> <foreign_key_clause_sub_2_2_> <foreign_key_clause_sub_2_>",
                                    ""],
    "<foreign_key_clause_sub_2_1_>": ["DELETE", "UPDATE"],
    "<foreign_key_clause_sub_2_2_>": ["SET NULL", "SET DEFAULT", "CASCADE", "RESTRICT", "NO ACTION"],

    "<foreign_key_clause_sub_3_>": ["MATCH <string_>", ""],

    "<foreign_key_clause_sub_4_>": ["<foreign_key_clause_sub_4_1_> <foreign_key_clause_sub_4_2_>", ""],
    "<foreign_key_clause_sub_4_1_>": ["DEFERRABLE", "NOT DEFERRABLE"],
    "<foreign_key_clause_sub_4_2_>": ["INITALLY DEFERRED", "INITIALLY IMMEDIATE", ""],

    "<conflict_clause_>": ["ON CONFLICT ROLLBACK", "ON CONFLICT ABORT", "ON CONFLICT FAIL", "ON CONFLICT IGNORE", "ON CONFLICT REPLACE", ""],

    "<indexed_columns_>": ["<indexed_column_>", "<indexed_column_>,<indexed_columns_>"],
    "<indexed_column_>": ["<indexed_column_sub_> <indexed_column_sub_2_> <asc_desc_>"],
    "<indexed_column_sub_>": ["<string_>", "<expr_>"],
    "<indexed_column_sub_2_>": ["COLLATE <string_>", ""],

    "<table_options_>": ["<table_option_>", "<table_option_>,<table_option_>"],
    "<table_option_>": ["STRICT", "WITHOUT ROWID"],

    "<update_statement_>": 
    ["<statement_start_with_> UPDATE <update_insert_or> <qualified_table_name_> SET <update_statement_sub_> <update_statement_from_> <update_delete_where_> <return_clauses_>;"],
    "<update_statement_sub_>": ["<string_>=<expr_>", "(<column_name_>)=<expr_>",
                                "<string_>=<expr_>,<update_statement_sub_>",
                                "(<column_name_>)=<expr_>,<update_statement_sub_>"],
    "<update_statement_from_>": ["FROM <table_or_sub_or_join_clause_>", ""],

    "<table_or_sub_or_join_clause_>": ["<table_or_subquery_>", "<join_clause_>"],

    "<update_insert_or>": ["OR ABORT", "OR FAIL", "OR IGNORE", "OR REPLACE", "OR ROLLBACK", ""],

    "<delete_statement_>": [
        "<statement_start_with_> DELETE FROM <qualified_table_name_> <update_delete_where_> <return_clauses_>;"],

    "<select_statement_>": [
        "<statement_start_with_> SELECT <select_statement_sub_> <result_columns_> FROM <table_name_> <result_columns_> <select_statement_from_> <select_statement_where_> <select_statement_group_by_> <select_statement_window_> <select_statement_order_by_> <select_statement_limit_>;",
        "<statement_start_with_> <select_statement_values_> <select_statement_order_by_> <select_statement_limit_>;",

    ],

    "<select_statement_sub_>": ["DISTINCT", "ALL", ""],
    "<select_statement_from_>": ["FROM <join_clause_>", "FROM <table_or_subqueries_>", ""],
    "<select_statement_where_>": ["WHERE <expr_>", ""],
    "<select_statement_order_by_>": ["ORDER BY <ordering_terms_>", ""],
    "<select_statement_limit_>": ["LIMIT <expr_> <select_statement_limit_sub_>", ""],
    "<select_statement_limit_sub_>": ["OFFSET <expr_>", ", <expr_>", ""],
    "<select_statement_values_>": ["VALUES (<exprs_>)", "VALUES (<exprs_>)(<exprs_>)"],
    "<select_statement_group_by_>": ["GROUP BY <exprs_>", "GROUP BY <exprs_> HAVING <expr_>", "HAVING <expr_>", ""],
    "<select_statement_window_>": ["WINDOW <select_statement_window_sub_>", ""],
    "<select_statement_window_sub_>": ["<string_> AS <window_defn_>",
                                       "<string_> AS <window_defn_>,<select_statement_window_sub_>"],

    "<qualified_table_name_>": ["<schema_table_name_> <indexed_not_indexed_>",
                                "<schema_table_name_> AS <string_> <indexed_not_indexed_>"],

    "<update_delete_where_>": ["WHERE <expr_>", ""],

    "<result_column_>": ["<expr_> <as_alias_>", "<table_name_>.",  ""],
    "<result_columns_>": ["<result_column_>", "<result_column_>,<result_columns_>"],
    "<as_alias_>": ["<string_>", "AS <string_>", ""],
    "<table_or_subqueries_>": ["<table_or_subquery_>", "<table_or_subquery_>,<table_or_subqueries_>"],
    
    "<table_or_subquery_>": ["<table_or_subquery_sub_> <indexed_not_indexed_>","<table_name_> (<exprs_>)", "<simple_functions_>(<exprs_>)", "(<select_statement_>)",
                             "(<select_statement_>) AS <table_alias_>", "(<select_statement_>) <table_alias_>", "(<table_or_subqueries_>)", "(<join_clause_>)"],
    "<table_or_subquery_sub_>": ["<schema_name_build_><table_name_build_>"],
    
    "<table_name_build_>": ["<table_name_>", "<table_name_> <table_alias_>", "<table_name_> AS <table_alias_>"],
    "<schema_name_build_>": ["<schema_name_>.", ""],
    "<indexed_not_indexed_>": ["INDEXED BY <string_>", "NOT INDEXED", ""],
    "<join_clause_>": ["<table_or_subquery_>", "<join_operator_> <table_or_subquery_> <join_constraint_>"],
    "<join_constraint_>": ["ON <expr_>", "USING (<column_name_>)", ""],
    "<join_operator_>": [",", "JOIN", "CROSS JOIN", "<join_operator_sub_>"],
    "<join_operator_sub_>": ["NATURAL JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN", "INNER JOIN",
                             "NATURAL LEFT JOIN", "NATURAL RIGHT JOIN", "NATURAL FULL JOIN", "NATURAL INNER JOIN",
                             "NATURAL LEFT OUTER JOIN", "NATURAL RIGHT OUTER JOIN", "NATURAL FULL OUTER JOIN"],

    "<begin_statement_>": ["BEGIN <begin_statement_sub_> <transaction_empty_>;"],
    "<begin_statement_sub_>": ["DEFERRED", "IMMEDIATE", "EXCLUSIVE", ""],

    "<commit_statement_>": ["<commit_statement_sub_> <transaction_empty_>;"],
    "<commit_statement_sub_>": ["COMMIT", "END"],

    "<rollback_statement_>": ["ROLLBACK <transaction_empty_>;",
                              "ROLLBACK <transaction_empty_> TO <savepoint_empty_> <string_>;"],

    "<pragma_statement_>": ["PRAGMA <pragma_statement_sub_> <pragma_statement_sub_1_>;"],
    "<pragma_statement_sub_>": ["<string_>", "<schema_name_>.<string_>"],
    "<pragma_statement_sub_1_>": ["= <pragma_value_>", "(<pragma_value_>)", ""],

    "<vacuum_statement_>": ["VACUUM <vacuum_statement_sub_> <vacuum_statement_sub_1_>;"],
    "<vacuum_statement_sub_>": ["<schema_name_>", ""],
    "<vacuum_statement_sub_1_>": ["INTO <string_>", ""],

    "<savepoint_statement_>": ["SAVEPOINT <string_>;"],
    "<release_savepoint_statement_>": ["RELEASE <savepoint_empty_> <string_>;"],

    "<analyse_statement_>": ["ANALYZE;", "ANALYZE <schema_name_>;", "ANALYZE <schema_table_name_>;"],

    "<create_view_>": [
        "CREATE <temp_temporary_> VIEW <if_not_exists_> <create_view_sub_> <create_view_sub_1_> AS <select_statement_>;"],

    "<create_view_sub_>": ["<schema_name_>.<string_>", "<string_>"],
    "<create_view_sub_1_>": ["(<column_name_>)", ""],

    "<drop_view_>": ["DROP VIEW <if_exists_> <drop_view_sub_>;"],

    "<drop_view_sub_>": ["<string_>", "<schema_name_>.<string_>"],

    "<create_virtual_table_>": [
        "CREATE VIRTUAL TABLE <if_not_exists_> <schema_table_name_> USING <string_> <create_virtual_table_sub_>;"],
    "<create_virtual_table_sub_>": ["(<module_argument_>)", ""],

    "<explain_statement_>": ["<explain_>"],
    "<explain_>": ["<explain_1_>", "<explain_1_><explain_>"],
    "<explain_1_>": ["<explain_statement_sub_> <explain_statement_sub_2_>"],

    "<explain_statement_sub_>": ["EXPLAIN", "EXPLAIN QUERY PLAN", ""],
    "<explain_statement_sub_2_>": ["<create_table_>", "<drop_table_>", "<alter_table_>", "<select_statement_>",
                                   "<insert_statement_>", "<delete_statement_>", "<update_statement_>",
                                   "<explain_statement_>", "<analyse_statement_>", "<begin_statement_>",
                                   "<commit_statement_>", "<rollback_statement_>", "<create_view_>", "<drop_view_>",
                                   "<create_virtual_table_>", "<create_index_>", "<drop_index_>", "<attach_database_>",
                                   "<detach_database_>", "<re_index_>", "<create_trigger_>", "<drop_trigger_>",
                                   "<pragma_statement_>", "<vacuum_statement_>", "<savepoint_statement_>",
                                   "<release_savepoint_statement_>"],

    "<create_index_>": [
        "CREATE <create_index_sub_> <if_not_exists_> <create_index_sub_1_> ON <table_name_> (<indexed_columns_>) <create_index_sub_2_>;"],
    "<create_index_sub_>": ["UNIQUE", ""],
    "<create_index_sub_1_>": ["<string_>", "<schema_name_>.<string_>"],
    "<create_index_sub_2_>": ["WHERE <expr_>", ""],

    "<drop_index_>": ["DROP INDEX <if_exists_> <drop_index_sub_>;"],
    "<drop_index_sub_>": ["<string_>", "<schema_name_>.<string_>"],

    "<re_index_>": ["REINDEX", "REINDEX <collation_name_>", "REINDEX <re_index_sub_>;"],
    "<re_index_sub_>": ["<table_name_>", "<string_>", "<schema_name_>.<table_name_>",
                        "<schema_name_>.<string_>"],

    "<attach_database_>": ["ATTACH <databases_sub_> <expr_> AS <schema_name_>;"],
    "<detach_database_>": ["DETACH <databases_sub_> <schema_name_>;"],
    "<databases_sub_>": ["DATABASE", ""],

    "<create_trigger_>": [
        "CREATE <temp_temporary_> TRIGGER <if_not_exists_> <schema_triggers_> <create_trigger_sub_> <create_trigger_sub_1_> ON <table_name_> <create_trigger_sub_2_> BEGIN <create_trigger_sub_3_> END"],
    "<create_trigger_sub_>": ["BEFORE", "AFTER", "INSTEAD OF", ""],
    "<create_trigger_sub_1_>": ["DELETE", "INSERT", "UPDATE", "UPDATE OF <column_name_>"],
    "<create_trigger_sub_2_>": ["FOR EACH ROW", "WHEN <expr_>", "FOR EACH ROW WHEN <expr_>", ""],
    "<create_trigger_sub_3_>": ["<create_trigger_sub_4_>", "<create_trigger_sub_4_> <create_trigger_sub_4_3"],
    "<create_trigger_sub_4_>": ["<update_statement_>", "<insert_statement_>", "<delete_statement_>",
                                "<select_statement_>"],

    "<drop_trigger_>": ["DROP TRIGGER <if_exists_> <schema_triggers_>;"],


    "<schema_triggers_>": ["<string_>", "<schema_name_>.<string_>"],

    "<statement_start_with_>": ["WITH <common_table_expressions_>", "WITH RECURSIVE <common_table_expressions_>", ""],

    "<exprs_paranthesis_>": ["(<exprs_>)", "(<exprs_paranthesis_sub_>)"],
    "<exprs_paranthesis_sub_>": ["(<expr_>)", "(<expr_>),<exprs_paranthesis_sub_>"],

    "<exprs_>": ["<expr_>", "<expr_>,<exprs_>"],

    "<expr_>": ["<literal_value_>",
                "<bind_parameter_>",
                "<schema_table_column_name_>",
                "<unary_operator_> <expr_>",
                "<expr_> <binary_operator_> <expr_>",
                "<aggregate_functions_>(<function_arguments_>) <filter_clause_> <over_clause_>",
                "(<exprs_>)",
                "CAST (<expr_> AS <type_name_>)",
                "<expr_> COLLATE <string_>",
                "<expr_> <expr_sub_> LIKE <expr_> <expr_sub_2_>",
                "<expr_> <expr_sub_> <expr_sub_1_> <expr_> <expr_sub_5_>",
                "<expr_> <is_null_not_null>",
                "<expr_> <expr_sub_3_> <expr_sub_4_> <expr_>",
                "<expr_> <expr_sub_6_> BETWEEN <expr_> AND <expr_>",
                "<expr_> <expr_sub_6_> <expr_sub_7_8_>",
                "<exists_not_exists_> (<select_statement_>)",
                "CASE <expr_sub_9_> <expr_sub_10_> <expr_sub_12_> END",
                "<raise_function_>"
                ],
    "<expr_sub_>": ["NOT", ""],
    "<expr_sub_1_>": ["GLOB", "REGEXP", "MATCH"],
    "<expr_sub_2_>": ["ESCAPE <expr_>", ""],
    "<expr_sub_3_>": ["IS", "IS NOT"],
    "<expr_sub_4_>": ["DISTINCT FROM", ""],
    "<expr_sub_5_>": ["ESCAPE <expr_>", ""],
    "<expr_sub_6_>": ["IN", "NOT IN"],
    "<expr_sub_7_8_>": ["<expr_sub_7_>", "<expr_sub_8_>"],
    "<expr_sub_7_>": ["(<select_statement_>)", "(<exprs_>)", "()"],
    "<expr_sub_8_>": ["<table_name_>", "<schema_name_>.<table_name_>"],
    "<expr_sub_9_>": ["<expr_>", ""],
    "<expr_sub_10_>": ["<expr_sub_11_>", "<expr_sub_11_> <expr_sub_10_>"],
    "<expr_sub_11_>": ["WHEN <expr_> THEN <expr_>"],
    "<expr_sub_12_>": ["ELSE <expr_>", ""],

    "<is_null_not_null>": ["ISNULL", "NOTNULL", "NOT NULL"],
    "<exists_not_exists_>": ["EXIST", "NOT EXIST", ""],

    "<schema_table_column_name_>": ["<string_>", "<string_>.<string_>",
                                    "<schema_name_>.<string_>.<string_>"],

    "<literal_value_>": ["<integer_>", "<string_>", "<blob_>", "NULL", "TRUE", "FALSE", "CURRENT_TIME", "CURRENT_DATE",
                         "CURRENT_TIMESTAMP"],

    "<filter_clause_>": ["FILTER (WHERE <expr_>)", ""],

    "<over_clause_>": ["OVER <string_>", "OVER (<over_clause_sub_> <over_clause_sub_partition_> <over_clause_sub_order_by_> <frame_spec_empy_>)", ""],
    "<over_clause_sub_>": ["<base_window_name_>", ""],
    "<over_clause_sub_partition_>": ["PARTITION BY <exprs_>", ""],
    "<over_clause_sub_order_by_>": ["ORDER BY <ordering_terms_>", ""],

    "<raise_function_>": ["RAISE (IGNORE)", "RAISE (<raise_function_sub_>,<string_>)"],
    "<raise_function_sub_>": ["ROLLBACK", "ABORT", "FAIL"],

   #  "<function_arguments_simple_>": ["<exprs_>", "*", ""],
    "<function_arguments_>": ["<function_arguments_sub_> <exprs_> <function_arguments_sub_1_>", "*", ""],
    "<function_arguments_sub_>": ["DISTINCT", ""],
    "<function_arguments_sub_1_>": ["ORDER BY <ordering_terms_>", ""],

    "<common_table_expressions_>": ["<common_table_expression_>",
                                    "<common_table_expression_>,<common_table_expressions_>"],
    
    "<common_table_expression_>": ["<table_name_> <as_not_materialised_> (<select_statement_>)", "<table_name_> (<column_name_>) <as_not_materialised_> (<select_statement_>)"],

    "<window_defn_>": ["(<base_window_name_> <window_partition_> <window_order_> <frame_spec_empy_>)"],
    "<window_partition_>": ["PARTITION BY <exprs_>", ""],
    "<window_order_>": ["ORDER BY <ordering_term_>", ""],
    "<base_window_name_>": ["<string_>", ""],

    "<ordering_terms_>": ["<ordering_term_>", "<ordering_term_>,<ordering_terms_>"],
    "<ordering_term_>": ["<expr_> <collation_name_> <asc_desc_> <null_first_last_>"],
    "<collation_name_>": ["COLLATE <string_>", ""],
    "<asc_desc_>": ["ASC", "DESC", ""],
    "<null_first_last_>": ["NULLS FIRST", "NULLS LAST", ""],

    
    "<frame_spec_empy_>": ["<frame_spec_>", ""],
    "<frame_spec_>": [
        "<frame_spec_sub_> BETWEEN <frame_spec_sub_between_> AND <frame_spec_sub_and_> <frame_spec_sub_3_>",
        "<frame_spec_sub_> <frame_spec_sub_2_> <frame_spec_sub_3_>"],

    "<frame_spec_sub_>": ["RANGE", "ROWS", "GROUPS"],
    "<frame_spec_sub_2_>": ["UNBOUNDED PRECEDING", "<expr_> PRECEDING", "CURRENT ROW"],
    "<frame_spec_sub_3_>": ["EXCLUDE NO OTHERS", "EXCLUDE CURRENT ROW", "EXCLUDE GROUP", "EXCLUDE TIES", ""],

    "<frame_spec_sub_between_>": ["UNBOUNDED PRECEDING", "<expr_> PRECEDING", "CURRENT ROW", "<expr_> FOLLOWING"],
    "<frame_spec_sub_and_>": ["<expr_> PRECEDING", "CURRENT ROW", "<expr_> FOLLOWING", "UNBOUNDED FOLLOWING"],

    "<schema_table_name_>": ["<table_name_>", "<schema_name_>.<table_name_>"],
    "<module_argument_>": ["<string_>", "<string_>,<module_argument_>"],

    "<return_clauses_>": ["RETURNING <return_clause_>", ""],
    "<return_clause_>": ["<return_clause_1_>", "<return_clause_1_>,<return_clause_>"],
    "<return_clause_1_>": ["*", "<expr_>", "<expr_> AS <string_>", "<expr_> <string_>"],

    
    "<aggregate_functions_>": ["avg", "count", "group concat", "min", "sum", "total", "max", "string_agg"],
     "<simple_functions_>": ["abs", "changes", "char", "coalesce", "concat", "concat_ws", "format", "glob", "hex",
                             "ifnull", "iif", "instr", "last_insert_rowid", "length", "like", "likelihood", "likely",
                             "load_extension", "lower", "ltrim", "ltrim", "max", "min", "nullif", "octet_length",
                             "printf", "quote", "random", "randomblob", "replace", "round", "rtrim", "sign", "soundex",
                             "sqlite_compileoption_get", "sqlite_compileoption_used", "sqlite_offset",
                             "sqlite_source_id", "sqlite_version", "substr", "substring", "total_changes", "trim",
                             "typeof", "unhex", "unicode", "unlikely", "upper", "zeroblob"],
    
    "<as_not_materialised_>": ["AS", "AS MATERIALIZED", "AS NOT MATERIALIZED"],
    "<transaction_empty_>": ["TRANSACTION", ""],
    "<savepoint_empty_>": ["SAVEPOINT", ""],
    "<pragma_value_>": ["<signed_number_>", "<string_>", "<signed_number_>"],
    "<temp_temporary_>": ["TEMP", "TEMPORARY", ""],
    "<if_exists_>": ["IF EXISTS", ""],
    "<if_not_exists_>": ["IF NOT EXISTS", ""],
    "<bind_parameter_>": ["?", "?<integer_>", ":<string_>", "@<string_>", "$<string_>"],
    "<unary_operator_>": ["+", "-", "~"],
    "<binary_operator_>": ["<", ">", "<=", ">=", "="],
    "<signed_number_>": ["<integer_>", "+<integer_>", "-<integer_>"],
    "<table_alias_>": ["<up_char_><string_>s"],
    "<table_name_>": ["<up_char_><string_>s"],
    "<column_name_>": ["<string_>", "<string_>,<column_name_>"],
    "<schema_name_>": ["<string_>", "<up_string_>"],


    "<integer_>": ["<digit_>", "<digit_><integer_>"],
    "<digit_>": ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],

    "<string_>": ["<char_>", "<char_><string_>"],
    "<char_>": ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                't', 'u', 'v', 'w', 'x', 'y', 'z'],

    "<blob_>": ["x<hex_chars_>", "X<hex_chars_>"],
    
    "<hex_chars_>": ["<hex_char_>", "<hex_char_><hex_chars_>"],
    "<hex_char_>": ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'],

    "<up_string_>": ["<up_char_>", "<up_char_><up_string_>"],
    "<up_char_>": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                   'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],

}