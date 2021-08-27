# techweirdo_python_assign

API details : 

# To get details of a medicine using either its id or name
## GET '/medicine/?id=1' : 

parameters : 
 <!-- Enter either name or id. Atleast one in mandatory. You can enter only one.  -->
    id : medicine_id
    name : medicine_name

response : 
    {
    "status": "sucess",
    "data": [
        {
            "id": 1,
            "name": "Medicine 1",
            "batch_no": "batch1",
            "mnf_date": "2021-08-01",
            "expire_date": "2022-08-01",
            "type": "capsule",
            "quantity_measurment": "piece"
        }
    ]
    }

# To add a new medicine to DB
## POST '/medicine/' : 

request body : 
    {
    "name" : "Medicine 4",
    "batch_no" : "batch4",
    "mnf_date" : "2021-08-02",
    "expire_date" : "2022-10-10",
    "type" : "tablet",
    "quantity_measurment" : "piece"
    }

response :
    {
    "status": "success",
    "msg": "Medicine details succesfully entered."
    }

# To get user details using either its id or first_name
## GET '/users/?first_name=user_1' : 

parameters : 
    <!-- Enter either first_name or id. Atleast one in mandatory. You can enter only one. -->
    id : user_id
    first_name : first_name

response : 
    {
    "status": "sucess",
    "data": [
        {
            "id": 1,
            "first_name": "user_1",
            "last_name": "new",
            "age": 24,
            "address": "bengaluru",
            "contact": "1234567890"
        },
        {
            "id": 2,
            "first_name": "user_1",
            "last_name": "new",
            "age": 24,
            "address": "bengaluru",
            "contact": "1234567890"
        }
    ]
    }

# To add a new user to the DB
## POST '/users' : 

request : 
    {
    "first_name" : "user_4",
    "last_name" : "new",
    "age" : 24,
    "address" : "bengaluru",
    "contact" : "1234567890"
    }

response : 
    {
    "status": "sucess",
    "msg": "User details succesfully entered."
    }

# To get what are the medicine one particular user is supposed to take given a particular date as parameter, and out of these which the users have already taken

## GET '/medicine/intake/?user=1&date=2021-08-25&status=taken' :

paramentrs : 
<!-- All parameters are complusury  -->
    user : user_id
    date : intake_date(date format)
    status : taken/not_taken

response : 
    {
    "status": "sucess",
    "data": [
        {
            "id": 3,
            "medicine_id": 1,
            "user_id": 1,
            "intake_time": "morning",
            "no_of_times_a_day": 2,
            "intake_date": "2021-08-25",
            "status": "taken",
            "quantity": "1"
        },
        {
            "id": 4,
            "medicine_id": 1,
            "user_id": 1,
            "intake_time": "evening",
            "no_of_times_a_day": 2,
            "intake_date": "2021-08-25",
            "status": "taken",
            "quantity": "1"
        }
    ]
    }

# To create a new medicine intake tracker
## POST '/medicine/intake/' :

request :
    {
    "intake_time" : "night",
    "no_of_times_a_day" : 1,
    "intake_date" : "2021-08-28",
    "medicine_id" : 3,
    "user_id" : 2,
    "quantity" : "10"
 }

 response :
 {
    "status": "sucess",
    "msg": "Medicine Intake detail for User : user_1  succesfully entered."
}

#  To mark one / multiple medicine as taken for a particular date at a given time
## PATCH '/medicine/intake/' :

request : 
[
    {"user":1, "medicine":1, "intake_time" : "morning", "date": "2021-08-25"},
    {"user":1, "medicine":1, "intake_time" : "evening", "date": "2021-08-25"},
    {"user":1, "medicine":2, "intake_time" : "evening", "date": "2021-08-26"},
    {"user":4, "medicine":4, "intake_time" : "morning", "date": "2021-08-25"}
]

response : 
{
    "status": "sucess",
    "msg": "All medicine intake for user list : [{'user_1': 'Medicine 1', 'intake_time': 'morning'}, {'user_1': 'Medicine 1', 'intake_time': 'evening'}, {'user_1': 'Medicine 2', 'intake_time': 'evening'}] sucessfully updated as taken."
}