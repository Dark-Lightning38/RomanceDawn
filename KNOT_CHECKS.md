#KNOT_CHECK week 1

#First breaking things:
Nothing happened when I deleted the tasks file except loosing my tasks history. When I launched the script I went on menu 2 "Show Tasks" and it answered "No tasks yet in the list!". JSON create the file if it doesn't exist. I guess.
I entered a "c" and it printed out "Invalid input. Please enter a number." as planned in script. YEAH !!
I pressed Ctrl-C mid session adding a task, it printed the menu & said "Goodbye". Too bad I'd rather it didn't reprint the menu.
I commented out remove_task2 and got this "Traceback (most recent call last): "NameError: name 'remove_task2' is not defined. Did you mean: 'remove_task'?" Interesting. logical......other liens explanable.

#Second fixing the bare except in day2OPTIONC an breaking things:
Why would a filenotfounderror make sense if anyway the file recreates ? or is it to prevent recreating a file froms cratch without knowing it ? I also added the json.JSONDecodeError, but what does it fix Claude ?

#Fixing/Resolving all my #WHY in code in day1.py
commented out the line 115 of day1.py as I created a dic to add that I didn't need in the end as I append manually in line 121. Same for line 142.

#Fixing/Resolving all my #WHY in code in day1.py
line 8 ok I unerstand the formula now, r is read.... logical...
line 15 ok too if it fails.. but with now lines 10 to 13 it may not be needed to be fair in a true dev context.
line 18  as a file is clear it assigns as a variable in the function. great !!
line 53 I think I finally understand//// if not (reverses the next argument True/False) list() which if empty is False... sor everse means true and the block of code int he if will execute 
lines70 to 74 ... fixed the issue I was having and lack of understanding as to why it worked that way. Wrong if/else construction.

#wrap input calls
ok so I do now understand the need ...and I've added it. I think it shoudl also be added to other scripts I have not just day1.py though.
