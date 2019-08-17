# RecepieDjango
Django Recepie Project

This Project handles all the CRUD operatios. This project has the following REST endpoints

1. createRecepie - For creating the new recepie using POST method. 
                   Full url when ran locally "http://localhost:8000/createRecepie
                   Example Data :
                                     {
	                                "username" : "Madhu",
	                                "name" : "Oats",
	                                "ingredients" : ["Oats", "salt","water", "chillies"],
	                                "steps" : ["Boil water and add Oats", "Add salt", "Mix well and serve"]
                                      }
      *NOTE: Since no specific data format/input is provided I assumes all the incoming data.
 
 2. getallRecepies - Get all the Recepies using GET method
                     Full URL : http://localhost:8000/getallRecepies
                  
 3. getRecepiesByUser -  Get all the Recepies by a particular user using GET method
                         Full URL : http://localhost:8000/getRecepiesByUser
                         Parameters needed: 
                                          username : <USER>

4. updateRecepies -  Update a Particular Recepie by a user using PUT method
                     Full url when ran locally "http://localhost:8000/updateRecepie
                     Example Data: {
	                                "username" : "Madhu",
	                                "name" : "Oats",
	                                "ingredients" : ["Oats", "salt","water", "chillies"],
	                                "steps" : ["Boil water and add Oats", "Add salt", "Mix well and serve"]
                                     }
 5. deleteRecepie:  Delete a particular Recepie using DELETE Method.
                    Full url when ran locally "http://localhost:8000/deleteRecepie
                    Paramters needed: 
                                     name : <RECEPIE-NAME>
 
 
                                      
                                     

