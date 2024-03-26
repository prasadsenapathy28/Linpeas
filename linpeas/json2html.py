import json
import sys
import random


def parse_json(json_data : object) -> str:
    """Parse the given json adding it to the HTML file"""
    
    body = ""
    i=1
    for key, value in json_data.items():
        body += """\t\t<button type="button" class="btn" data-toggle="collapse" data-target="#demo"""+ str(i) + "\"><b>" + key + """</button></b><br>\n
        <div id="demo"""+ str(i)+ """\" class="collapse">\n"""
        i=i+1
        for key1, value1 in value.items():
            
            if(type(value1)==list):
                body+=parse_list(value1)
            
            if((type(value1)==dict)):
                body+=parse_dict(value1)
        body+="\t\t\t</div>\n"
    
    return body


def parse_dict(json_dict: dict) -> str:
    """Parse the given dict from the given json adding it to the HTML file"""

    dict_text=""
    for key, value in json_dict.items():
        n=random.randint(0,999999)
        infos = []
        for info in value["infos"]:
            if info.startswith("http"):
                infos.append(f"<a href='{info}'>{info}</a><br>\n")
            else:
                infos.append(str(info) + "<br>\n")
                
        dict_text += f'\t\t<button type="button" class="btn1" data-toggle="collapse" data-target="#lines{n}">{key}</button><br>\n'
        dict_text += '<i>' + "".join(infos) + '</i>'
        dict_text += f'<div id="lines{n}" class="collapse1">\n'
        
        if value["lines"]:
            dict_text+="\n" + parse_list(value["lines"]) + "\n"

        if value["sections"]:
            dict_text+=parse_dict(value["sections"])
            
    return dict_text


def parse_list(json_list: list) -> str:
    """Parse the given list from the given json adding it to the HTML file"""
    color_text=""
    color_class=""

    for i in json_list:
        if "═══" not in i['clean_text']:
            if(i['clean_text']):
                color_text+= "<div class = \""
                text = str(i['clean_text'])
                for color in i['colors']:
                    if(color=='BLUE'):
                        style = "#0000FF"
                        color_class = "blue"
                    if(color=='LIGHT_GREY'):
                        style = "#adadad"
                        color_class = "light_grey"
                    if(color=='REDYELLOW'):
                        style = "#FF0000; background-color: #FFFF00;"
                        color_class = "redyellow"
                    if(color=='RED'):
                        style = "#FF0000"
                        color_class = "red"
                    if(color=='GREEN'):
                        style = "#008000"
                        color_class = "green"
                    if(color=='MAGENTA'):
                        style = "#FF00FF"
                        color_class = "magenta"
                    if(color=='YELLOW'):
                        style = "#FFFF00"
                        color_class = "yellow"
                    if(color=='DARKGREY'):
                        style = "#A9A9A9"
                        color_class = "darkgrey"
                    if(color=='CYAN'):
                        style = "#00FFFF"
                        color_class = "cyan"
                    for replacement in i['colors'][color]:
                        text=text.replace(replacement," <b style=\"color:"+ style +"\">"+ replacement + "</b>")
                        #class=\""+ color_class + "\" "+ "
                        if "═╣" in text:
                            text=text.replace("═╣","<li>")
                            text+="</li>"
                    color_text+=  "" + color_class + " " 
                color_text +="no_color\" >"+ text + "<br></div>\n"                
    return color_text + "\t\t\t</div>\n"


def main():
    with open(JSON_PATH) as JSON_file:
        json_data = json.load(JSON_file)
        html = HTML_HEADER
        html += HTML_INIT_BODY
        html += parse_json(json_data)
        html += HTML_END
    
    with open(HTML_PATH, 'w') as f:
        f.write(html)



HTML_HEADER = """
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1" charset="UTF-8">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
        <style>
            .btn {
            border-radius: 2px;
            border: 2px solid #000000;
            background-color: #33adff;
            color: white;
            padding: 8px 16px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 8px 40%;
            transition-duration: 0.4s;
            cursor: pointer;
            border-radius: 8px;
            
            }

            .btn1 {
            border-radius: 2px;
            border: 2px solid #000000;
            background-color: #33adff;
            color: white;
            padding: 4px 8px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 8px 4px;
            transition-duration: 0.4s;
            cursor: pointer;
            border-radius: 8px;
            
            }

            .btn:hover {
                box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
                background-color: #6fd1ff;
                color: white;
            }

            .btn1:hover {
                box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
                background-color: #6fd1ff;
                color: white;
            }

            .collapse {
                margin: 15px 8%;
                padding: 8px 8px;
                border: 1px solid #000000;
                width: 80%;
                background-color: #adebad;
            }
            
            .collapse1 {
                margin: 15px 8%;
                padding: 8px 8px;
                border: 2px solid #000000;
                width: 80%;
                background-color: #91ff96;
            }

            .peass_image{
                display: block;
				margin-left:30%;
                margin-right:30%;
				width: 30%;
            }
            
            .div_redyellow{
                
                margin-left:35%;
                margin-right:35%; 
            }

            .btn_redyellow{
                background-color: #FFFF00;
                padding: 4px 8px;
                border-radius: 8px;
                color:#FF0000;
                border:2px solid #FF0000;
            }

            .btn_redyellow:hover {
                box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
                background-color: #FF0000;
                border: 2px solid #FF0000;
                color: #FFFF00;
                transition-duration: 0.4s;
            }
            
            .btn_red_redyellow{
                background: #FFFF00;
                padding: 4px 8px;
                border-radius: 8px;
                color:#FF0000;
                border:2px solid #FF0000;
            }

            .btn_red_redyellow:hover {
                box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
                background: #FF0000;
                border: 2px solid #FF0000;
                color: #FFFF00;
                transition-duration: 0.4s;
            }
            
            .btn_restore, .btn_show_all, .btn_hide_all{
                margin-top: 3px;
                border-radius: 2px;
                padding: 4px 8px;
                background-color: #00ff15;
                border: 2px solid #06660e;
                border-radius: 8px;
            }

            .btn_restore:hover, .btn_show_all:hover, .btn_hide_all:hover{
                box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
                border: 2px solid #00ff15;
                color: #00ff15;
                transition-duration: 0.4s;
                background: rgb(300, 300, 300);
            }

            body{
                background-color: #91ff96
            }

        </style>
    </head>

"""

HTML_END = """
        <script>
            
            $(document).ready(() => {
                $('.btn_show_all').click(function() {
                    show_all();
                });
                $('.btn_hide_all').click(function() {
                    hide_all();
                });
                $('.btn_redyellow').click(function() {
                    only_redyellow();
                });
                $('.btn_red_redyellow').click(function() {
                    only_red_redyellow();
                });
                $('.btn_restore').click(function() {
                    restore();
                });
            });
            function show_all(){
                $('.collapse').show();
            }
            function hide_all(){
                $('.collapse').hide();
            }
            function only_redyellow(){
                $('.red').hide();
                $('.light_grey').hide();
                $('.blue').hide();
                $('.green').hide();
                $('.magenta').hide();
                $('.yellow').hide();
                $('.darkgrey').hide();
                $('.cyan').hide();
                $('.no_color').hide();
                $('.redyellow').show();
            }

            function only_red_redyellow(){

                $('.light_grey').hide();
                $('.blue').hide();
                $('.green').hide();
                $('.magenta').hide();
                $('.yellow').hide();
                $('.darkgrey').hide();
                $('.cyan').hide();
                $('.no_color').hide();
                $('.red').show();
                $('.redyellow').show();
            }

            function restore(){

                $('.light_grey').show();
                $('.blue').show();
                $('.green').show();
                $('.magenta').show();
                $('.yellow').show();
                $('.darkgrey').show();
                $('.cyan').show();
                $('.no_color').show();
                $('.red').show();
                $('.redyellow').show();
            }
        </script>
    </body>
</html>"""

HTML_INIT_BODY = body = """
    <body>
        <br>
        <div class = "div_redyellow">
            <button type="button" class="btn_redyellow"> Only RedYellow </button>
            <button type="button" class="btn_red_redyellow"> Only Red + RedYellow </button><br>
            <button type="button" class="btn_restore"> All Colors </button>
            <button type="button" class="btn_show_all"> Show All </button>
            <button type="button" class="btn_hide_all"> Hide All </button>
        </div>"""


# Start execution
if __name__ == "__main__":
    try:
        JSON_PATH = sys.argv[1]
        HTML_PATH = sys.argv[2]
    except IndexError as err:
        print("Error: Please pass the peas.json file and the path to save the html\npeas2html.py <json_file.json> <HTML_file.html>")
        sys.exit(1)
    
    main()