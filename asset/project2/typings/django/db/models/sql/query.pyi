"""
This type stub file was generated by pyright.
"""

from django.db.models.expressions import BaseExpression
from django.utils.functional import cached_property

"""
Create SQL statements for QuerySets.

The code in here encapsulates all of the SQL construction so that QuerySets
themselves do not have to (and could be backed by things other than SQL
databases). The abstraction barrier only works one way: this module has to know
all about the internals of models in order to get the information it needs.
"""
__all__ = ['Query', 'RawQuery']
def get_field_names_from_opts(opts): # -> set[Unknown]:
    ...

def get_children_from_q(q): # -> Generator[Unknown, None, None]:
    ...

JoinInfo = ...
class RawQuery:
    """A single raw SQL query."""
    def __init__(self, sql, using, params=...) -> None:
        ...
    
    def chain(self, using): # -> RawQuery:
        ...
    
    def clone(self, using): # -> RawQuery:
        ...
    
    def get_columns(self): # -> list[Any | Unknown]:
        ...
    
    def __iter__(self): # -> Iterator[Unknown]:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    @property
    def params_type(self): # -> Type[dict[Unknown, Unknown]] | Type[tuple[Unknown, ...]] | None:
        ...
    
    def __str__(self) -> str:
        ...
    


ExplainInfo = ...
class Query(BaseExpression):
    """A single SQL query."""
    alias_prefix = ...
    empty_result_set_value = ...
    subq_aliases = ...
    compiler = ...
    def __init__(self, model, alias_cols=...) -> None:
        ...
    
    @property
    def output_field(self): # -> Any | None:
        ...
    
    @property
    def has_select_fields(self): # -> bool:
        ...
    
    @cached_property
    def base_table(self): # -> None:
        ...
    
    def __str__(self) -> str:
        """
        Return the query as a string of SQL with the parameter values
        substituted in (use sql_with_params() to see the unsubstituted string).

        Parameter values won't necessarily be quoted correctly, since that is
        done by the database interface at execution time.
        """
        ...
    
    def sql_with_params(self): # -> Any:
        """
        Return the query as an SQL string and the parameters that will be
        substituted into the query.
        """
        ...
    
    def __deepcopy__(self, memo): # -> Empty:
        """Limit the amount of work when a Query is deepcopied."""
        ...
    
    def get_compiler(self, using=..., connection=..., elide_empty=...): # -> Any:
        ...
    
    def get_meta(self):
        """
        Return the Options instance (the model._meta) from which to start
        processing. Normally, this is self.model._meta, but it can be changed
        by subclasses.
        """
        ...
    
    def clone(self): # -> Empty:
        """
        Return a copy of the current Query. A lightweight alternative to
        to deepcopy().
        """
        ...
    
    def chain(self, klass=...): # -> Empty:
        """
        Return a copy of the current Query that's ready for another operation.
        The klass argument changes the type of the Query, e.g. UpdateQuery.
        """
        ...
    
    def relabeled_clone(self, change_map): # -> Empty:
        ...
    
    def rewrite_cols(self, annotation, col_cnt):
        ...
    
    def get_aggregation(self, using, added_aggregate_names):
        """
        Return the dictionary with the values of the existing aggregations.
        """
        ...
    
    def get_count(self, using): # -> Literal[0]:
        """
        Perform a COUNT() query using the current filter constraints.
        """
        ...
    
    def has_filters(self): # -> WhereNode:
        ...
    
    def exists(self, using, limit=...): # -> Empty:
        ...
    
    def has_results(self, using):
        ...
    
    def explain(self, using, format=..., **options): # -> str:
        ...
    
    def combine(self, rhs, connector):
        """
        Merge the 'rhs' query into the current one (with any 'rhs' effects
        being applied *after* (that is, "to the right of") anything in the
        current query. 'rhs' is not modified during a call to this function.

        The 'connector' parameter describes how to connect filters from the
        'rhs' query.
        """
        ...
    
    def deferred_to_data(self, target, callback):
        """
        Convert the self.deferred_loading data structure to an alternate data
        structure, describing the field that *will* be loaded. This is used to
        compute the columns to select from the database and also by the
        QuerySet class to work out which fields are being initialized on each
        model. Models that have all their fields included aren't mentioned in
        the result, only those that have field restrictions in place.

        The "target" parameter is the instance that is populated (in place).
        The "callback" is a function that is called whenever a (model, field)
        pair need to be added to "target". It accepts three parameters:
        "target", and the model and list of fields being added for that model.
        """
        ...
    
    def table_alias(self, table_name, create=..., filtered_relation=...): # -> tuple[Unknown, Literal[False]] | tuple[str | Unknown, Literal[True]]:
        """
        Return a table alias for the given table_name and whether this is a
        new alias or not.

        If 'create' is true, a new alias is always created. Otherwise, the
        most recently created alias for the table (if one exists) is reused.
        """
        ...
    
    def ref_alias(self, alias): # -> None:
        """Increases the reference count for this alias."""
        ...
    
    def unref_alias(self, alias, amount=...): # -> None:
        """Decreases the reference count for this alias."""
        ...
    
    def promote_joins(self, aliases):
        """
        Promote recursively the join type of given aliases and its children to
        an outer join. If 'unconditional' is False, only promote the join if
        it is nullable or the parent join is an outer join.

        The children promotion is done to avoid join chains that contain a LOUTER
        b INNER c. So, if we have currently a INNER b INNER c and a->b is promoted,
        then we must also promote b->c automatically, or otherwise the promotion
        of a->b doesn't actually change anything in the query results.
        """
        ...
    
    def demote_joins(self, aliases): # -> None:
        """
        Change join type from LOUTER to INNER for all joins in aliases.

        Similarly to promote_joins(), this method must ensure no join chains
        containing first an outer, then an inner join are generated. If we
        are demoting b->c join in chain a LOUTER b LOUTER c then we must
        demote a->b automatically, or otherwise the demotion of b->c doesn't
        actually change anything in the query results. .
        """
        ...
    
    def reset_refcounts(self, to_counts): # -> None:
        """
        Reset reference counts for aliases so that they match the value passed
        in `to_counts`.
        """
        ...
    
    def change_aliases(self, change_map):
        """
        Change the aliases in change_map (which maps old-alias -> new-alias),
        relabelling any references to them in select columns and the where
        clause.
        """
        ...
    
    def bump_prefix(self, outer_query): # -> None:
        """
        Change the alias prefix to the next letter in the alphabet in a way
        that the outer query's aliases and this query's aliases will not
        conflict. Even tables that previously had no alias will get an alias
        after this call.
        """
        ...
    
    def get_initial_alias(self): # -> cached_property | str | None:
        """
        Return the first alias for this query, after increasing its reference
        count.
        """
        ...
    
    def count_active_tables(self): # -> int:
        """
        Return the number of tables in this query with a non-zero reference
        count. After execution, the reference counts are zeroed, so tables
        added in compiler will not be seen by this method.
        """
        ...
    
    def join(self, join, reuse=...):
        """
        Return an alias for the 'join', either reusing an existing alias for
        that join or creating a new one. 'join' is either a
        sql.datastructures.BaseTable or Join.

        The 'reuse' parameter can be either None which means all joins are
        reusable, or it can be a set containing the aliases that can be reused.

        A join is always created as LOUTER if the lhs alias is LOUTER to make
        sure chains like t1 LOUTER t2 INNER t3 aren't generated. All new
        joins are created as LOUTER if the join is nullable.
        """
        ...
    
    def join_parent_model(self, opts, model, alias, seen):
        """
        Make sure the given 'model' is joined in the query. If 'model' isn't
        a parent of 'opts' or if it is None this method is a no-op.

        The 'alias' is the root alias for starting the join, 'seen' is a dict
        of model -> alias of existing joins. It must also contain a mapping
        of None -> some alias. This will be returned in the no-op case.
        """
        ...
    
    def add_annotation(self, annotation, alias, is_summary=..., select=...): # -> None:
        """Add a single annotation expression to the Query."""
        ...
    
    def resolve_expression(self, query, *args, **kwargs):
        ...
    
    def get_external_cols(self): # -> list[Col | Unknown]:
        ...
    
    def as_sql(self, compiler, connection): # -> tuple[Any | Unknown, Any | Unknown]:
        ...
    
    def resolve_lookup_value(self, value, can_reuse, allow_joins): # -> list[Unknown] | tuple[Unknown, ...]:
        ...
    
    def solve_lookup_type(self, lookup): # -> tuple[Unknown | tuple[()], tuple[()], Unknown] | tuple[Unknown, Unknown, Literal[False]]:
        """
        Solve the lookup type from the lookup (e.g.: 'foobar__id__icontains').
        """
        ...
    
    def check_query_object_type(self, value, opts, field): # -> None:
        """
        Check whether the object passed while querying is of the correct type.
        If not, raise a ValueError specifying the wrong object.
        """
        ...
    
    def check_related_objects(self, field, value, opts): # -> None:
        """Check the type of object passed to query relations."""
        ...
    
    def check_filterable(self, expression): # -> None:
        """Raise an error if expression cannot be used in a WHERE clause."""
        ...
    
    def build_lookup(self, lookups, lhs, rhs):
        """
        Try to extract transforms and lookup from given lhs.

        The lhs value is something that works like SQLExpression.
        The rhs value is what the lookup is going to compare against.
        The lookups is a list of names to extract using get_lookup()
        and get_transform().
        """
        ...
    
    def try_transform(self, lhs, name):
        """
        Helper method for build_lookup(). Try to fetch and initialize
        a transform for name parameter from lhs.
        """
        ...
    
    def build_filter(self, filter_expr, branch_negated=..., current_negated=..., can_reuse=..., allow_joins=..., split_subq=..., check_filterable=...):
        """
        Build a WhereNode for a single filter clause but don't add it
        to this Query. Query.add_q() will then add this filter to the where
        Node.

        The 'branch_negated' tells us if the current branch contains any
        negations. This will be used to determine if subqueries are needed.

        The 'current_negated' is used to determine if the current filter is
        negated or not and this will be used to determine if IS NULL filtering
        is needed.

        The difference between current_negated and branch_negated is that
        branch_negated is set on first negation, but current_negated is
        flipped for each negation.

        Note that add_filter will not do any negating itself, that is done
        upper in the code by add_q().

        The 'can_reuse' is a set of reusable joins for multijoins.

        The method will create a filter clause that can be added to the current
        query. However, if the filter isn't added to the query then the caller
        is responsible for unreffing the joins used.
        """
        ...
    
    def add_filter(self, filter_lhs, filter_rhs): # -> None:
        ...
    
    def add_q(self, q_object): # -> None:
        """
        A preprocessor for the internal _add_q(). Responsible for doing final
        join promotion.
        """
        ...
    
    def build_where(self, filter_expr): # -> WhereNode:
        ...
    
    def clear_where(self): # -> None:
        ...
    
    def build_filtered_relation_q(self, q_object, reuse, branch_negated=..., current_negated=...): # -> WhereNode:
        """Add a FilteredRelation object to the current filter."""
        ...
    
    def add_filtered_relation(self, filtered_relation, alias): # -> None:
        ...
    
    def names_to_path(self, names, opts, allow_many=..., fail_on_missing=...):
        """
        Walk the list of names and turns them into PathInfo tuples. A single
        name in 'names' can generate multiple PathInfos (m2m, for example).

        'names' is the path of names to travel, 'opts' is the model Options we
        start the name resolving from, 'allow_many' is as for setup_joins().
        If fail_on_missing is set to True, then a name that can't be resolved
        will generate a FieldError.

        Return a list of PathInfo tuples. In addition return the final field
        (the last used join field) and target (which is a field guaranteed to
        contain the same value as the final field). Finally, return those names
        that weren't found (which are likely transforms and the final lookup).
        """
        ...
    
    def setup_joins(self, names, opts, alias, can_reuse=..., allow_many=...):
        """
        Compute the necessary table joins for the passage through the fields
        given in 'names'. 'opts' is the Options class for the current model
        (which gives the table we are starting from), 'alias' is the alias for
        the table to start the joining from.

        The 'can_reuse' defines the reverse foreign key joins we can reuse. It
        can be None in which case all joins are reusable or a set of aliases
        that can be reused. Note that non-reverse foreign keys are always
        reusable when using setup_joins().

        If 'allow_many' is False, then any reverse foreign key seen will
        generate a MultiJoin exception.

        Return the final field involved in the joins, the target field (used
        for any 'where' constraint), the final 'opts' value, the joins, the
        field path traveled to generate the joins, and a transform function
        that takes a field and alias and is equivalent to `field.get_col(alias)`
        in the simple case but wraps field transforms if they were included in
        names.

        The target field is the field containing the concrete value. Final
        field can be something different, for example foreign key pointing to
        that value. Final field is needed for example in some value
        conversions (convert 'obj' in fk__id=obj to pk val using the foreign
        key field for example).
        """
        ...
    
    def trim_joins(self, targets, joins, path): # -> tuple[Unknown | tuple[Unknown, ...], Unknown, Unknown]:
        """
        The 'target' parameter is the final field being joined to, 'joins'
        is the full list of join aliases. The 'path' contain the PathInfos
        used to create the joins.

        Return the final target field and table alias and the new active
        joins.

        Always trim any direct join if the target column is already in the
        previous table. Can't trim reverse joins as it's unknown if there's
        anything on the other side of the join.
        """
        ...
    
    def resolve_ref(self, name, allow_joins=..., reuse=..., summarize=...): # -> Ref:
        ...
    
    def split_exclude(self, filter_expr, can_reuse, names_with_path): # -> tuple[Unknown, Unknown]:
        """
        When doing an exclude against any kind of N-to-many relation, we need
        to use a subquery. This method constructs the nested query, given the
        original exclude filter (filter_expr) and the portion up to the first
        N-to-many relation field.

        For example, if the origin filter is ~Q(child__name='foo'), filter_expr
        is ('child__name', 'foo') and can_reuse is a set of joins usable for
        filters in the original query.

        We will turn this into equivalent of:
            WHERE NOT EXISTS(
                SELECT 1
                FROM child
                WHERE name = 'foo' AND child.parent_id = parent.id
                LIMIT 1
            )
        """
        ...
    
    def set_empty(self): # -> None:
        ...
    
    def is_empty(self): # -> bool:
        ...
    
    def set_limits(self, low=..., high=...): # -> None:
        """
        Adjust the limits on the rows retrieved. Use low/high to set these,
        as it makes it more Pythonic to read and write. When the SQL query is
        created, convert them to the appropriate offset and limit values.

        Apply any limits passed in here to the existing constraints. Add low
        to the current low value and clamp both to any existing high value.
        """
        ...
    
    def clear_limits(self): # -> None:
        """Clear any existing limits."""
        ...
    
    @property
    def is_sliced(self): # -> bool:
        ...
    
    def has_limit_one(self): # -> Literal[False]:
        ...
    
    def can_filter(self): # -> bool:
        """
        Return True if adding filters to this instance is still possible.

        Typically, this means no limits or offsets have been put on the results.
        """
        ...
    
    def clear_select_clause(self): # -> None:
        """Remove all fields from SELECT clause."""
        ...
    
    def clear_select_fields(self): # -> None:
        """
        Clear the list of fields to select (but not extra_select columns).
        Some queryset types completely replace any existing list of select
        columns.
        """
        ...
    
    def add_select_col(self, col, name): # -> None:
        ...
    
    def set_select(self, cols): # -> None:
        ...
    
    def add_distinct_fields(self, *field_names): # -> None:
        """
        Add and resolve the given fields to the query's "distinct on" clause.
        """
        ...
    
    def add_fields(self, field_names, allow_m2m=...):
        """
        Add the given (model) fields to the select set. Add the field names in
        the order specified.
        """
        ...
    
    def add_ordering(self, *ordering):
        """
        Add items from the 'ordering' sequence to the query's "order by"
        clause. These items are either field names (not column names) --
        possibly with a direction prefix ('-' or '?') -- or OrderBy
        expressions.

        If 'ordering' is empty, clear all ordering from the query.
        """
        ...
    
    def clear_ordering(self, force=..., clear_default=...): # -> None:
        """
        Remove any ordering settings if the current query allows it without
        side effects, set 'force' to True to clear the ordering regardless.
        If 'clear_default' is True, there will be no ordering in the resulting
        query (not even the model's default).
        """
        ...
    
    def set_group_by(self, allow_aliases=...):
        """
        Expand the GROUP BY clause required by the query.

        This will usually be the set of all non-aggregate fields in the
        return data. If the database backend supports grouping by the
        primary key, and the query would be equivalent, the optimization
        will be made automatically.
        """
        ...
    
    def add_select_related(self, fields): # -> None:
        """
        Set up the select_related data structure so that we only select
        certain related models (as opposed to all models, when
        self.select_related=True).
        """
        ...
    
    def add_extra(self, select, select_params, where, params, tables, order_by):
        """
        Add data to the various extra_* attributes for user-created additions
        to the query.
        """
        ...
    
    def clear_deferred_loading(self): # -> None:
        """Remove any fields from the deferred loading set."""
        ...
    
    def add_deferred_loading(self, field_names): # -> None:
        """
        Add the given list of model field names to the set of fields to
        exclude from loading from the database when automatic column selection
        is done. Add the new field names to any existing field names that
        are deferred (or removed from any existing field names that are marked
        as the only ones for immediate loading).
        """
        ...
    
    def add_immediate_loading(self, field_names): # -> None:
        """
        Add the given list of model field names to the set of fields to
        retrieve when the SQL is executed ("immediate loading" fields). The
        field names replace any existing immediate loading field names. If
        there are field names already specified for deferred loading, remove
        those names from the new field_names before storing the new names
        for immediate loading. (That is, immediate loading overrides any
        existing immediate values, but respects existing deferrals.)
        """
        ...
    
    def get_loaded_field_names(self): # -> dict[Unknown, Unknown]:
        """
        If any fields are marked to be deferred, return a dictionary mapping
        models to a set of names in those fields that will be loaded. If a
        model is not in the returned dictionary, none of its fields are
        deferred.

        If no fields are marked for deferral, return an empty dictionary.
        """
        ...
    
    def get_loaded_field_names_cb(self, target, model, fields): # -> None:
        """Callback used by get_deferred_field_names()."""
        ...
    
    def set_annotation_mask(self, names): # -> None:
        """Set the mask of annotations that will be returned by the SELECT."""
        ...
    
    def append_annotation_mask(self, names): # -> None:
        ...
    
    def set_extra_mask(self, names): # -> None:
        """
        Set the mask of extra select items that will be returned by SELECT.
        Don't remove them from the Query since they might be used later.
        """
        ...
    
    def set_values(self, fields):
        ...
    
    @property
    def annotation_select(self): # -> dict[Unknown, Unknown]:
        """
        Return the dictionary of aggregate columns that are not masked and
        should be used in the SELECT clause. Cache this result for performance.
        """
        ...
    
    @property
    def extra_select(self): # -> dict[Unknown, Unknown]:
        ...
    
    def trim_start(self, names_with_path):
        """
        Trim joins from the start of the join path. The candidates for trim
        are the PathInfos in names_with_path structure that are m2m joins.

        Also set the select column so the start matches the join.

        This method is meant to be used for generating the subquery joins &
        cols in split_exclude().

        Return a lookup usable for doing outerq.filter(lookup=self) and a
        boolean indicating if the joins in the prefix contain a LEFT OUTER join.
        _"""
        ...
    
    def is_nullable(self, field): # -> Any:
        """
        Check if the given field should be treated as nullable.

        Some backends treat '' as null and Django treats such fields as
        nullable for those backends. In such situations field.null can be
        False even if we should treat the field as nullable.
        """
        ...
    


def get_order_dir(field, default=...): # -> tuple[Unknown, Unknown]:
    """
    Return the field name and direction for an order specification. For
    example, '-foo' is returned as ('foo', 'DESC').

    The 'default' param is used to indicate which way no prefix (or a '+'
    prefix) should sort. The '-' prefix always sorts the opposite way.
    """
    ...

def add_to_dict(data, key, value): # -> None:
    """
    Add "value" to the set of values for "key", whether or not "key" already
    exists.
    """
    ...

def is_reverse_o2o(field): # -> bool:
    """
    Check if the given field is reverse-o2o. The field is expected to be some
    sort of relation field or related object.
    """
    ...

class JoinPromoter:
    """
    A class to abstract away join promotion problems for complex filter
    conditions.
    """
    def __init__(self, connector, num_children, negated) -> None:
        ...
    
    def add_votes(self, votes): # -> None:
        """
        Add single vote per item to self.votes. Parameter can be any
        iterable.
        """
        ...
    
    def update_join_types(self, query):
        """
        Change join types so that the generated query is as efficient as
        possible, but still correct. So, change as many joins as possible
        to INNER, but don't make OUTER joins INNER if that could remove
        results from the query.
        """
        ...
    


