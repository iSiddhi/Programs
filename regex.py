import re
import re
value="this is a string"
output=re.search("^This.*string$",value)
print(output)

pattern = r"^(?=.[a-z])(?=.[A-Z])(?=.[!@#$%^&()_+=-])(?=.{8,})"
