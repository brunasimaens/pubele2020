import jinja2  as j2

t = j2.Template( """
<html>
<head>
  <title> {{tit}} </title>
  <meta charset="UTF-8"/>
</head>
<body>
 <h1> {{tit}} </h1>
 <h2>Autores</h2>
 <hr/>
 <ol>
    {% for nome,email in auts    %}
      <li> {{nome}} : {{email}} </li>
    {% endfor %}
 </ol>
 <hr/>
</body>
</html>

"""
)


print(t.render( tit="Relatório 1", auts=[
   ("JJ","jj@di"),
   ("PM","pedro@di"),
   ("JA","Joao@di"),
   ("Ana","Ana@di"),
  ]))
