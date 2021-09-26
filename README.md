# Elevator Algorithm
Python implementation of a basic elevator system.

The system consists of three main entities: Elevator System, Floor System and Elevator Dispatcher, each one of them share and interact with basic objects, such as Buttons, Doors, Motors, and a Motoring system.

To run the system go to [Running system](#Running-system).

The main considerations are the following:

* **Floor / Hall Buttons**: Each button is a type of a generic button, it has ON and OFF state that can be associated to a light indicator, from a specific floor, pressing this button will call the closest available elevator, and keeps on until the elevator has arrived at the floor.
* **Elevator buttons**: Each button is a type of a generic button, with a numeric label of the destination floor, it has ON and OFF state that can be associated to a light indicator as well, pressing this button will move the elevator to the destination floor.
* **Doors**: they can either be open or close, they can change status from inside elevator, when the elevator reaches the destination floor (from an elevator button or from a floor request) the door will be open from an amount of time and then will close.
* **Motor**: It determines whether the elevator is moving or not, and its direction UP or DOWN, the direction will be determined by the Elevator System, an emergency stop is also implemented, it stops the motion and opens the door. 
The elevator can move only in the initialized number of floors and cannot move if the door is open.
* **Monitoring system**: The overall system reports the actions into the console and into a LOG file, the logger was configured in the way that we know what methods/functions were executed and the state of the elevators.

### Generalized elevator pseudocode 
From inside the elevator:
```
Elevator status is set to idle (no motion) current floor is 0 and door is close.
if the floor button press, activate button
find the direction of motor UP or DOWN
while current floor is not desired floor:
    motion started, elevator motor state change to moving UP/DOWN
    motion stop, elevator motor state change to IDLE
    elevator current floor increase/decrease depending on direction
    repeat
    end while
Elevator reaches desired floor, deactivate button
Open door for some seconds
Close door
Repeat.
```
# Running system
The system was developed/tested with Python 3 (tested with 3.5, 3.8 and 3.9) and can be tested in three different ways:
* `run.py` script
* Interactive python console
* API

Whichever the case, a `elevator_system.log` file will be generated with all the actions
### Script

The `run.py` script shows an overall functionality of the system including some special cases:

With python 3 run:
```bash
python src/run.py
```
### Interactive python console
Locate into src folder, start python interpreter or open an interactive console, eg. `IPython`.

Then. import the modules, start an instance of classes and test behavior in real time:

```python
from Motor import MotorState
from Dispatcher import ElevatorDispatcher
from Floor import FloorSystem
from Elevator import ElevatorSystem
import Log as log
logger = log.setup_logger()
NUMBER_OF_FLOORS  =  7
dispatcher =  ElevatorDispatcher()  # dispatcher
elevator_1 =  ElevatorSystem(idx=1,  number_of_floors=NUMBER_OF_FLOORS)
elevator_2 =  ElevatorSystem(idx=2,  number_of_floors=NUMBER_OF_FLOORS)
floors = FloorSystem.generate_floors(NUMBER_OF_FLOORS)

elevator_1.press_elevator_button(3)
floors[2].call_elevator_from_floor(elevator_2)
requested_floor =  3
floors[requested_floor].call_elevator_from_floor(
    dispatcher.request_elevator_from_floor(
        requested_floor,  [elevator_1, elevator_2]
    )
)
elevator_1
```

## API

A basic API/REST was implemented to run the system in an infinite loop, this provides a convenient simulation of the elevators and halls. The elevators can be monitored in real time.

In order to run the API make sure to have Flask installed on your environment:

    pip install Flask

**RUN API**

    python src/run_api.py

### Endpoints:

* **GET** - [http://127.0.0.1:5000/check](http://127.0.0.1:5000/check) - Check current state of elevators

* **GET** - [http://127.0.0.1:5000/call_elevator/floor/3](http://127.0.0.1:5000/call_elevator/floor/3) - Call elevator from specified floor

* **POST** - [http://127.0.0.1:5000/elevator/](http://127.0.0.1:5000/elevator/) - JSON Body - Press floor button from inside elevator

#### Examples:
#### GET http://127.0.0.1:5000/check

This endpoint shows the current state of elevators

```bash
$ curl http://127.0.0.1:5000/check/
>> {
  "1": {
    "elevator_id": 1,
    "current_floor": 2,
    "motor_state": "Motor state: IDLE",
    "door": "Door is: Close"
  },
  "2": {
    "elevator_id": 2,
    "current_floor": 6,
    "motor_state": "Motor state: IDLE",
    "door": "Door is: Close"
  }
}
```

#### GET http://127.0.0.1:5000/call_elevator/floor/3

This endpoint request an elevator from a floor.

To request an elevator from floor 5 run:
```bash
$ curl http://127.0.0.1:5000/call_elevator/floor/5
>> {
  "message": "Elevator Requested from FLOOR 5"
}
```
You can use the previous endpoint con confirm that the nearest elevator changed to floor 5.

#### POST http://127.0.0.1:5000/check

To simulate floor buttons from inside elevator you can send a POST request with the following json body:

```json
{
    "elevator_id": 1,
    "button_press": 1
}
```

Example with CURL

```bash
curl --location --request POST 'http://127.0.0.1:5000/elevator/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "elevator_id": 2,
    "button_press": 2
}'

>> {
    "message": "Elevator 2 - button pressed: 2"
}
```


## Motoring
The logs are served using the logging python package with the following formatter:

    "%(asctime)s - [%(filename)s:%(module)s:%(lineno)s - %(funcName)s ] - %(levelname)s - %(message)s"

**Example of logs**:

```log
...
2021-09-25 14:56:54,748 - [run_api.py:run_api:77 - check_elevators ] - INFO - Check state of elevators from API
2021-09-25 16:47:07,148 - [run_api.py:run_api:90 - check_elevators ] - INFO - ELEVATOR: 
[ Elevator ID ]: 1
[Current Floor]: 2
[    State    ]: Motor state: IDLE
[    Door     ]: Door is: Close
2021-09-25 16:47:07,149 - [run_api.py:run_api:90 - check_elevators ] - INFO - ELEVATOR: 
[ Elevator ID ]: 2
[Current Floor]: 6
[    State    ]: Motor state: IDLE
[    Door     ]: Door is: Close
2021-09-25 16:49:40,497 - [run_api.py:run_api:63 - floor_action ] - INFO - Elevator Requested from FLOOR 3
2021-09-25 16:49:40,498 - [Dispatcher.py:Dispatcher:47 - request_elevator_from_floor ] - INFO - Selected Elevator: 1
2021-09-25 16:49:40,498 - [Floor.py:Floor:56 - call_elevator_from_floor ] - INFO - Elevator requested from floor 3
2021-09-25 16:49:40,498 - [Floor.py:Floor:58 - call_elevator_from_floor ] - INFO - Floor button Hall Button ButtonDirection.CALL: ON
2021-09-25 16:49:40,498 - [Elevator.py:Elevator:73 - move_one_floor ] - INFO - Elevator motor: MotorState.UP
2021-09-25 16:49:41,003 - [Elevator.py:Elevator:82 - move_one_floor ] - INFO - Elevator motor: MotorState.IDLE
2021-09-25 16:49:41,004 - [Elevator.py:Elevator:39 - open_and_close_door ] - INFO - Door is: Open
2021-09-25 16:49:42,018 - [Elevator.py:Elevator:43 - open_and_close_door ] - INFO - Door is: Close
2021-09-25 16:49:42,019 - [Floor.py:Floor:61 - call_elevator_from_floor ] - INFO - Floor button Hall Button ButtonDirection.CALL: OFF
...
```

And all the logs are stored in the `elevator_system.log` file located in the directory from the app was executed (repo root, src or other).
