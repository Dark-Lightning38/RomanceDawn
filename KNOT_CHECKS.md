#KNOT_CHECK week 1 & 2 - 2026-05-05

#First breaking things:
Nothing happened when I deleted the tasks file except loosing my tasks history. When I launched the script I went on menu 2 "Show Tasks" and it answered "No tasks yet in the list!". JSON create the file if it doesn't exist. I guess.
I entered a "c" and it printed out "Invalid input. Please enter a number." as planned in script. YEAH !!
I pressed Ctrl-C mid session adding a task, it printed the menu & said "Goodbye". Too bad I'd rather it didn't reprint the menu.
I commented out remove_task2 and got this "Traceback (most recent call last): "NameError: name 'remove_task2' is not defined. Did you mean: 'remove_task'?" Interesting. logical......other liens explanable.

#Second fixing the bare except in day2OPTIONC an breaking things:
Why would a filenotfounderror make sense if anyway the file recreates ? or is it to prevent recreating a file froms cratch without knowing it ? I also added the json.JSONDecodeError, but what does it fix Claude ?

#Fixing/Resolving all my #WHY in code in day1.py
commented out the line 115 of day1.py as I created a dic to add that I didn't need in the end as I append manually in line 121. Same for line 142.
line 120 I read about the tuple/map/split

#Fixing/Resolving all my #WHY in code in day1.py
line 8 ok I unerstand the formula now, r is read.... logical...
line 15 ok too if it fails.. but with now lines 10 to 13 it may not be needed to be fair in a true dev context.
line 18  as a file is clear it assigns as a variable in the function. great !!
line 53 I think I finally understand//// if not (reverses the next argument True/False) list() which if empty is False... sor everse means true and the block of code int he if will execute 
lines70 to 74 ... fixed the issue I was having and lack of understanding as to why it worked that way. Wrong if/else construction.
line 78 fixed my #WHY comment

#wrap input calls
ok so I do now understand the need ...and I've added it. I think it shoudl also be added to other scripts I have not just day1.py though.

#CLOSING 3 SENTENCES
surprised about the if __name__ == "__main--": method and it makes sense. better... I didn't know about the import method back then. so it suprised em the improtance of it. and that I had amde a mistake in lines 70 to 74 of day2OPTIONC.py as I had really checked - so good all in all.
learned the open ... as file fixing the file as variabel for Json very interesting. The if not list.Tuple,map & split method I had copied.
not confident about....rememberign all of that... from scratch end of day 3 will be a lot. and return in function.

#KNOT_CHECK week 3 - 2026-05-06

#First reading of code
I realized some stuff from yesterday like adding the "if __name__ == "__main__":"
added an #WHY where i'd like your answer how does the response.json work without import json
I see your point on the verify = False but CANNOT take the verify=False out as I am on a corporate network and it won't work otherwise


#Breaking things & fix
I entered "sdsfg" in city and the result was "sdsfg not found" and back to menu. ok that works then.
I entered 999 as hours but got the except classic that is now in line 63 ane 64... so I commented it out and got the except exception from lines 84 and 85. Instead of Value error encoded in lines 59/60. Can you explain that ?? Is it because the the final Except takes precendenc on the except in the nested formula ?
line 51 to 54 fixed for  cod 200 issue, makes sense actually now I understand that it would not have worked if no key present... makes sense.... hard ot remember that in future but ok.
timeout added
all except changes made..and it makes sense value error is wrong input for example, key error is when dealing with list/dict, and timeout error makes sense too so deos connection...exception as e ok it's other basically haha
verify = False CANNOT take the verify=False out as I am on a corporate network and it won't work otherwise
internet break undoable today.
Good news = nothing crashes.

#CLOSING 3 sentences
Surprised about the python script using .json without import first
learned more about try/except and learned more about error types. AND remembered I can do math within a list or key call liek [x//3] interesting.
Not confident about Remembering all the syntax of all functions..... how do people do ??? we say Task manager from scratch for example but I need to remember all syntax by heart ?

#Week 3: Post review fixes previous lines numbers no longer apply 
Ok it makes sense to put the if name around the lyon block and no the key. Changed.
Ok Index Error wouldn't be picked-up I get it now and fixed on lines 60/61
data funct fixed by putting before the except Exception as e.

#KNOT_CHECK week 4 - 2026-05-12

#Five tests I think about
1//day1 input empty for name in self_add_agent3
2//day1 input number without coma for hours worked in self_add_agent3
3//day2OPTIONC liens 141 to &55 what if we have a json error ? or in the 17 to 19 but what about if the file doesn't exist when teh save_tasks is happenign post launch of the script
4//Day3 enter a + as a city name
5//Day3 enter -3 in hours hehe

#so test results and fixes
1//Ok empty name worked....that is not good  
2// 45 saved it as (45,)
3//I deleted the task file after having launched the menu; then add task, then..................IT CAME BACK !! the file and previous task ??? how does that work ???
4// just + not found... it was a bad test... teh real test is inputting 120 and it tells me it's out of range...index error planned. shoudl I ahve fixed with a-1 in the code ??? maybe not..
5//HAHAHAHAHHA -3 actually gave me an answer for Lyon but went backward hahahaha ok, I should probably fix that too

1// fixed
2//I mean I could use the method I used for the worked days but same issue really.....so for the moemnt I think I'll leave it like this as I do not know a method to avoid this.
3// nothing to do hehehe
4// same nothing to fix in the end
5// At first I was thinking to use abs() but that is just forcing something that makes no sense so elt's fix with an if function.

#All bare except: have been removed.

#Added Index error to remove_trask2 as there is already an If condition above but asked for gating.

#READ ME v1 done

#VENV test passed and requirements.txt file updated

#today learning, surprised and not confident about
today I was surprised by how much after a week of vacation I still remembered the github command line
I learned about venv hehe
I am not confident about my remembering of certain formulas like the json ones..

#Now the big question at end of Phase 1
Yes I can do it.
Would I remember everyt construction or every trick no... but can I build it again and this time make it clean with no issues and explain every line and construction to a stranger.
I think in terms of gaps I would remember exactly how to write a load file or save and would need to refer to my notes or how to load the env file without looking at the formula os.etc. but otherwise I feel ok with everyhting else.