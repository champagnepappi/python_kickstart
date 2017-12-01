kevin = { "name": "Kevin", "homework": ["css", "js"],"tests": [] }
shaz = {"name": "sharon", "homework": ["react", "pyhton"], "tests": "lisp"}
santos = { "languages" : ["ruby", "python", "java"], "level": "junior dev" }

students = [kevin, shaz]

for student in students:
    print student["name"]
    print student["homework"]
    print student["tests"]
