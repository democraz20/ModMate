# ***Modmate***

## usage
press "Get profiles" once to load all the avaliable profiles using the minecraft path entered </br>
select a profile in the dropdown and click start

## setting up
The ModMate folder lives in your Minecraft's folder with the tree


## File structure
```
.minecraft
├── Modmate
│   ├── Mods
│   │   ├── mod1.jar
│   │   └── mod2.jar
│   ├── Profiles
│   │   ├── profile1.json
│   │   └── profile2.json
│   └── config
└── Mods
```
```\Modmate\Mods``` is where all the mods you have will be store </br>
```\Modmate\Profiles``` is where all the profiles you have will be store

all of this lives in your .minecraft folder of choice and </br>
files selected by the profile will automatically be copied to ```.minecraft\Mods```

to use, run
```
python main.py
```

a GUI should be opened up if you wish to use the CLI version instead, change 
```py
main("gui")
```
to 
```py
main("cli")
```
in ```main.py``` and vice verca