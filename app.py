from flask import Flask, request, render_template_string, jsonify
import ply.lex as lex
import ply.yacc as yacc

app = Flask(__name__)

# Lexer
tokens = (
    'CLASS', 'PUBLIC', 'STATIC', 'VOID', 'MAIN', 'SYSTEM', 'OUT', 'PRINTLN',
    'IDENTIFIER', 'NUMBER', 'PLUS', 'EQUALS',
    'SEMICOLON', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'DOT', 'STRING', 'LBRACKET', 'RBRACKET'
)

reserved = {
    'class': 'CLASS',
    'public': 'PUBLIC',
    'static': 'STATIC',
    'void': 'VOID',
    'main': 'MAIN',
    'System': 'SYSTEM',
    'out': 'OUT',
    'println': 'PRINTLN'
}

tokens += tuple(reserved.values())

t_PLUS = r'\+'
t_EQUALS = r'='
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_DOT = r'\.'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser
def p_program(p):
    '''program : class_decl'''
    pass

def p_class_decl(p):
    '''class_decl : PUBLIC CLASS IDENTIFIER LBRACE method_decl RBRACE'''
    pass

def p_method_decl(p):
    '''method_decl : PUBLIC STATIC VOID MAIN LPAREN parameter RPAREN LBRACE statements RBRACE'''
    pass

def p_parameter(p):
    '''parameter : IDENTIFIER LBRACKET RBRACKET IDENTIFIER'''
    pass

def p_statements(p):
    '''statements : statement
                  | statement statements'''
    pass

def p_statement(p):
    '''statement : SYSTEM DOT OUT DOT PRINTLN LPAREN STRING RPAREN SEMICOLON
                 | IDENTIFIER EQUALS expression SEMICOLON
                 | IDENTIFIER SEMICOLON'''
    pass

def p_expression(p):
    '''expression : term
                  | term PLUS term'''
    pass

def p_term(p):
    '''term : IDENTIFIER
            | NUMBER
            | STRING'''
    pass

def p_error(p):
    if p:
        error_message = f"Syntax error at '{p.value}', line {p.lineno}. "
        if p.type == 'SEMICOLON':
            error_message += "Missing semicolon."
        elif p.type == 'EQUALS':
            error_message += "Missing equals sign."
        elif p.type == 'PLUS':
            error_message += "Missing term after plus sign."
        else:
            error_message += "Syntax error."
        parser.error = error_message
    else:
        parser.error = "Syntax error at EOF"

parser = yacc.yacc()
parser.error = None

@app.route('/analyze', methods=['POST'])
def analyze():
    code = request.json.get('code', '')
    lexer.input(code)
    
    tokens_list = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_list.append({
            'type': tok.type,
            'value': tok.value,
            'lineno': tok.lineno,
            'lexpos': tok.lexpos
        })

    parser.error = None
    parser.parse(code)
    if parser.error:
        parse_result = parser.error
    else:
        parse_result = 'Código correcto!'

    return jsonify({'tokens': tokens_list, 'message': parse_result})

@app.route('/', methods=['GET', 'POST'])
def index():
    code = ""
    lexical_result = []
    syntactic_result = ""
    if request.method == 'POST':
        if 'code' in request.form and request.form['code'].strip() != '':
            code = request.form['code']
        else:
            return "No code provided"
        
        lexer.input(code)
        while True:
            tok = lexer.token()
            if not tok:
                break
            lexical_result.append((tok.lineno, tok.lexpos, tok.type, tok.value))

        parser.error = None
        parser.parse(code)
        if parser.error:
            syntactic_result = parser.error
        else:
            syntactic_result = 'Código correcto!'
    
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Analizador Léxico y Sintáctico</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    </head>
    <body>
        <div class="header">
            <h1>Analizador Léxico y Sintáctico</h1>
        </div>
        <div class="container">
            <form method="POST">
                <textarea name="code" id="code" placeholder="Escribe tu código aquí...">{{ code }}</textarea>
                <div class="button-container">
                    <button type="submit">Análisis Léxico y Sintáctico</button>
                </div>
            </form>
            <div class="output">
                <h2>Resultado Léxico</h2>
                <pre id="lexicoResult">{{ lexical_result }}</pre>
                <h2>Resultado Sintáctico</h2>
                <pre id="sintacticoResult">{{ syntactic_result }}</pre>
            </div>
        </div>
    </body>
    </html>
    """, code=code, lexical_result=lexical_result, syntactic_result=syntactic_result)

if __name__ == '__main__':
    app.run(debug=True)
