from pyscript import document, display

def make_a_message(e): #e for event handling
    name = document.getElementById("input1").value #gets input1 value & stores in name variable
    age = document.getElementById("input2").value #gets input2 value & stores in age variable
    school = document.getElementById("input3").value #gets input3 value & stores in school variable
    #creating multiline string
    result = f'''👤 Student Profile: \n
    \tName: {name}
    \tAge: {age}
    \tSchool: {school}
    \n
    ✏️ Notes: \n
    {name} is currently {age} years old and studies at {school}.'''
    display(result, target = "output")