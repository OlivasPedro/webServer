from flask import Flask, send_file

app = Flask(__name__)

@app.route('/download/<string:boleto_nome>')
def download_boleto(boleto_nome):
    
    # Construa o caminho do boleto com base no nome
    boleto_path = f'C:/Users/pedro/Desktop/dacte/{boleto_nome}.pdf'
    
    # Define o nome do arquivo a ser baixado
    filename = f'{boleto_nome}.pdf'
    
    # Retorna o arquivo como um anexo para download
    return send_file(boleto_path, as_attachment=True, download_name=filename)

if __name__ == '__main__':
    app.run(debug=True)
