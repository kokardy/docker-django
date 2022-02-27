"""
This type stub file was generated by pyright.
"""

from enum import Enum

"""
This type stub file was generated by pyright.
"""
FILTER_SEPARATOR = ...
FILTER_ARGUMENT_SEPARATOR = ...
VARIABLE_ATTRIBUTE_SEPARATOR = ...
BLOCK_TAG_START = ...
BLOCK_TAG_END = ...
VARIABLE_TAG_START = ...
VARIABLE_TAG_END = ...
COMMENT_TAG_START = ...
COMMENT_TAG_END = ...
SINGLE_BRACE_START = ...
SINGLE_BRACE_END = ...
UNKNOWN_SOURCE = ...
tag_re = ...
logger = ...
class TokenType(Enum):
    TEXT = ...
    VAR = ...
    BLOCK = ...
    COMMENT = ...


class VariableDoesNotExist(Exception):
    def __init__(self, msg, params=...) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    


class Origin:
    def __init__(self, name, template_name=..., loader=...) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self):
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    @property
    def loader_name(self):
        ...
    


class Template:
    def __init__(self, template_string, origin=..., name=..., engine=...) -> None:
        ...
    
    def __iter__(self):
        ...
    
    def __repr__(self):
        ...
    
    def render(self, context):
        "Display stage -- can be called many times"
        ...
    
    def compile_nodelist(self):
        """
        Parse and compile the template source into a nodelist. If debug
        is True and an exception occurs during parsing, the exception is
        annotated with contextual line information where it occurred in the
        template source.
        """
        ...
    
    def get_exception_info(self, exception, token):
        """
        Return a dictionary containing contextual line information of where
        the exception occurred in the template. The following information is
        provided:

        message
            The message of the exception raised.

        source_lines
            The lines before, after, and including the line the exception
            occurred on.

        line
            The line number the exception occurred on.

        before, during, after
            The line the exception occurred on split into three parts:
            1. The content before the token that raised the error.
            2. The token that raised the error.
            3. The content after the token that raised the error.

        total
            The number of lines in source_lines.

        top
            The line number where source_lines starts.

        bottom
            The line number where source_lines ends.

        start
            The start position of the token in the template source.

        end
            The end position of the token in the template source.
        """
        ...
    


def linebreak_iter(template_source):
    ...

class Token:
    def __init__(self, token_type, contents, position=..., lineno=...) -> None:
        """
        A token representing a string from the template.

        token_type
            A TokenType, either .TEXT, .VAR, .BLOCK, or .COMMENT.

        contents
            The token source string.

        position
            An optional tuple containing the start and end index of the token
            in the template source. This is used for traceback information
            when debug is on.

        lineno
            The line number the token appears on in the template source.
            This is used for traceback information and gettext files.
        """
        ...
    
    def __repr__(self):
        ...
    
    def split_contents(self):
        ...
    


class Lexer:
    def __init__(self, template_string) -> None:
        ...
    
    def __repr__(self):
        ...
    
    def tokenize(self):
        """
        Return a list of tokens from a given template_string.
        """
        ...
    
    def create_token(self, token_string, position, lineno, in_tag):
        """
        Convert the given token string into a new Token object and return it.
        If in_tag is True, we are processing something that matched a tag,
        otherwise it should be treated as a literal string.
        """
        ...
    


class DebugLexer(Lexer):
    def tokenize(self):
        """
        Split a template string into tokens and annotates each token with its
        start and end position in the source. This is slower than the default
        lexer so only use it when debug is True.
        """
        ...
    


class Parser:
    def __init__(self, tokens, libraries=..., builtins=..., origin=...) -> None:
        ...
    
    def __repr__(self):
        ...
    
    def parse(self, parse_until=...):
        """
        Iterate through the parser tokens and compiles each one into a node.

        If parse_until is provided, parsing will stop once one of the
        specified tokens has been reached. This is formatted as a list of
        tokens, e.g. ['elif', 'else', 'endif']. If no matching token is
        reached, raise an exception with the unclosed block tag details.
        """
        ...
    
    def skip_past(self, endtag):
        ...
    
    def extend_nodelist(self, nodelist, node, token):
        ...
    
    def error(self, token, e):
        """
        Return an exception annotated with the originating token. Since the
        parser can be called recursively, check if a token is already set. This
        ensures the innermost token is highlighted if an exception occurs,
        e.g. a compile error within the body of an if statement.
        """
        ...
    
    def invalid_block_tag(self, token, command, parse_until=...):
        ...
    
    def unclosed_block_tag(self, parse_until):
        ...
    
    def next_token(self):
        ...
    
    def prepend_token(self, token):
        ...
    
    def delete_first_token(self):
        ...
    
    def add_library(self, lib):
        ...
    
    def compile_filter(self, token):
        """
        Convenient wrapper for FilterExpression
        """
        ...
    
    def find_filter(self, filter_name):
        ...
    


constant_string = ...
constant_string = ...
filter_raw_string = ...
filter_re = ...
class FilterExpression:
    """
    Parse a variable token and its optional filters (all as a single string),
    and return a list of tuples of the filter name and arguments.
    Sample::

        >>> token = 'variable|default:"Default value"|date:"Y-m-d"'
        >>> p = Parser('')
        >>> fe = FilterExpression(token, p)
        >>> len(fe.filters)
        2
        >>> fe.var
        <Variable: 'variable'>
    """
    def __init__(self, token, parser) -> None:
        ...
    
    def resolve(self, context, ignore_failures=...):
        ...
    
    def args_check(name, func, provided):
        ...
    
    args_check = ...
    def __str__(self) -> str:
        ...
    
    def __repr__(self):
        ...
    


class Variable:
    """
    A template variable, resolvable against a given context. The variable may
    be a hard-coded string (if it begins and ends with single or double quote
    marks)::

        >>> c = {'article': {'section':'News'}}
        >>> Variable('article.section').resolve(c)
        'News'
        >>> Variable('article').resolve(c)
        {'section': 'News'}
        >>> class AClass: pass
        >>> c = AClass()
        >>> c.article = AClass()
        >>> c.article.section = 'News'

    (The example assumes VARIABLE_ATTRIBUTE_SEPARATOR is '.')
    """
    def __init__(self, var) -> None:
        ...
    
    def resolve(self, context):
        """Resolve this variable against a given context."""
        ...
    
    def __repr__(self):
        ...
    
    def __str__(self) -> str:
        ...
    


class Node:
    must_be_first = ...
    child_nodelists = ...
    token = ...
    def render(self, context):
        """
        Return the node rendered as a string.
        """
        ...
    
    def render_annotated(self, context):
        """
        Render the node. If debug is True and an exception occurs during
        rendering, the exception is annotated with contextual line information
        where it occurred in the template. For internal usage this method is
        preferred over using the render method directly.
        """
        ...
    
    def __iter__(self):
        ...
    
    def get_nodes_by_type(self, nodetype):
        """
        Return a list of all nodes (within this node and its nodelist)
        of the given type
        """
        ...
    


class NodeList(list):
    contains_nontext = ...
    def render(self, context):
        ...
    
    def get_nodes_by_type(self, nodetype):
        "Return a list of all nodes of the given type"
        ...
    


class TextNode(Node):
    child_nodelists = ...
    def __init__(self, s) -> None:
        ...
    
    def __repr__(self):
        ...
    
    def render(self, context):
        ...
    
    def render_annotated(self, context):
        """
        Return the given value.

        The default implementation of this method handles exceptions raised
        during rendering, which is not necessary for text nodes.
        """
        ...
    


def render_value_in_context(value, context):
    """
    Convert any value to a string to become part of a rendered template. This
    means escaping, if required, and conversion to a string. If value is a
    string, it's expected to already be translated.
    """
    ...

class VariableNode(Node):
    child_nodelists = ...
    def __init__(self, filter_expression) -> None:
        ...
    
    def __repr__(self):
        ...
    
    def render(self, context):
        ...
    


kwarg_re = ...
def token_kwargs(bits, parser, support_legacy=...):
    """
    Parse token keyword arguments and return a dictionary of the arguments
    retrieved from the ``bits`` token list.

    `bits` is a list containing the remainder of the token (split by spaces)
    that is to be checked for arguments. Valid arguments are removed from this
    list.

    `support_legacy` - if True, the legacy format ``1 as foo`` is accepted.
    Otherwise, only the standard ``foo=1`` format is allowed.

    There is no requirement for all remaining token ``bits`` to be keyword
    arguments, so return the dictionary as soon as an invalid argument format
    is reached.
    """
    ...

