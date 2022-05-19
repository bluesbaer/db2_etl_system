# db2_etl_system   
A very simple ETL Tool for DB2   
   
This project contains 2 folder:   
tools:  This folder contains the executables    
template: This folder contains the parameter for the executables    
    
There is also a file caled RUN_WORKFLOW.py which runs the etl workflow.    
    
How To Use:    
Copy the folder template to an other name.    
Preferable to a name which gives a hint what data it is for.    
Copy the RUN_WORKFLOW.py to an other name corresponding to your template copy.    
    
Inside your new template folder you will find some python programs which contain the parameter to steer the etl process.    
1. extract.py  
Contains the necessary information to read from database, csv, json or fixedlength file    
2. preformat.py    
Contains the parameter to bring the data in an format which you want.    
3. filter.py    
Contains the parameter to filter all the data you want to process further.    
4. merge.py    
Contains all the parameter to join this data with other data    
5. cleanse.py    
Contains all the information to cleanse the data    
6. transform.py   
Is under construction    
7. delta.py    
Is under construction    
8. build.py    
Is under construction    
9. load.py    
Is under construction    
    
In your new RUN_WORKFLOW-File (PERSONAL_WORKFLOW.py for instance) you have to change the name template to your name of the template.    
    
Execute:    
python PERSONAL_WORKFLOW.py    
    
There is no need to change anything in the tools-folder.    
Except for debugging, implement new functionality, performance-changes, etc.    
If you change anything please keep me informed.    
info@manfred-wagner.at    

