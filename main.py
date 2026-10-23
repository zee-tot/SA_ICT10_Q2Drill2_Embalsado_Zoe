from pyscript import document

# design for the form
document.body.style.backgroundColor = "#fff0f5"
output = document.querySelector("#output")
output.style.backgroundColor = "#ffd6e5"
output.style.color = "#5a2a3c"
button = document.querySelector(".btn")
button.style.backgroundColor = "#f4a6c0"
button.style.borderColor = "#f4a6c0"
button.style.color = "#5a2a3c"

# Sets for each grade level from G7 to G10
grade7 = {"Sianna Santiago", "Nyle Gutierrez"}
grade8 = {"Sophia Pedro", "Eliesha Bulo"}
grade9 = {"Mikaela Cuevas", "Ethan Park"}
grade10 = {"Zoe Embalsado", "Stefan Pada"}

# Combines all the grade sets into one master set using the union set operator
members = grade7 | grade8 | grade9 | grade10


def result_checker(event):
    global members

    # It gets the output and values of the first and last name input fields
    first = document.querySelector("#first_name").value
    last = document.querySelector("#last_name").value

# Makes the first letter of each name uppercase and the rest lowercase
    first = document.querySelector("#first_name").value.title()
    last = document.querySelector("#last_name").value.title()

    # Adds the new member inside a set
    # The difference removes the member if the name is blank
    new_member = {f"{first} {last}".strip()} - {""}

    # This adds the new member to the master set using the union set operator
    members = members | new_member

    # Shows the full list and the total number of members
    all_members = "<br>".join(sorted(members))
    output.innerHTML = f"<b>Members:</b><br>{all_members}<br><br><b>Total members:</b> {len(members)}"