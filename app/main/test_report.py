import json

from flask import request, render_template

from app.utils.docx import set_sand_docxtpl
from config import Config
from . import main


@main.route('/test_report/', methods=['GET', 'POST'])
def test_report():
    if request.method == 'POST':
        file_location = Config.SAVE_DOCUMENT_PATH
        origin_data = request.get_data()
        str_data = str(origin_data, encoding='utf-8')
        dict_data = json.loads(str_data)

        with open(file_location + 'data.json', 'w') as f:
            json.dump(dict_data, f)

        set_sand_docxtpl(dict_data)
        return "数据"
    else:
        return render_template('test_report.html')


@main.route('/update_report/', methods=['GET'])
def update_report():
    file_location = Config.SAVE_DOCUMENT_PATH
    location=request.args.get('location')

    with open(file_location + 'data.json', 'r') as f:
        dict_data = json.load(f)
    try:
        set_sand_docxtpl(dict_data,location)
        return "成功"
    except Exception as e:
        print(str(e))
        return str(e)
