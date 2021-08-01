from agentplus_header import MAX_LABEL_COST,_MAX_NUMBER_OF_NODES,_MAX_NUMBER_OF_LINKS,_MAX_NUMBER_OF_TIME_INTERVALS,_MAX_NUMBER_OF_VEHICLES,_MAX_NUMBER_OF_PASSENGERS,_MAX_NUMBER_OF_SERVED_PASSENGERS,_MAX_NUMBER_OF_STATES,g_number_of_passengers,_MAX_NUMBER_OF_OUTBOUND_NODES
#from agentplus_header import *
g_pFileDebugLog = None
g_pFile_OutputAgentLog = None
g_pFile_OutputNodeLog = None
g_pFile_OutputLinkLog = None
g_pFileOutputLog = None
g_pFileAgentPathLog = None
g_pFile_Output_paxprofitLog = None
g_pFile_PathLog = None
g_pFile_Vehicle_Path_PassengerLog = None
# maps are implement with an empty dictionary
g_internal_node_no_map = {}
g_external_node_id_map = {}
g_internal_agent_no_map = {}
g_external_passenger_id_map = {}
g_external_vehicle_id_map = {}

g_number_of_threads = 4
# passenger info in Node as pickup and dropoff node are all passengers
g_node_passenger_id = [None] * _MAX_NUMBER_OF_NODES
g_node_type = [None] * _MAX_NUMBER_OF_NODES  # key nodeid 1: pick up, 2: drop off
g_node_timestamp = [None] * _MAX_NUMBER_OF_NODES  # key nodeid, values type 1: pick up:ready time, 2: order time
g_node_baseprofit = [None] * _MAX_NUMBER_OF_NODES  # type 2 = 0
# the number of outbound nodes. key nodeid, values type 1: pick up:ready time, 2: order time
g_outbound_node_size = [None] * _MAX_NUMBER_OF_NODES
pax_id_to_seq_no_map = {}  # std::map<int, int>

g_passenger_base_profit = [-7] * _MAX_NUMBER_OF_PASSENGERS
local_vehicle_passenger_additional_profit = [[0 for i in range(_MAX_NUMBER_OF_VEHICLES)] for j in
                                             range(_MAX_NUMBER_OF_PASSENGERS)]

g_passenger_order_time = [0] * _MAX_NUMBER_OF_PASSENGERS
# used in profit(LR multipliers) update: summation of variable y
g_passenger_number_of_visits = [0] * _MAX_NUMBER_OF_PASSENGERS
g_passenger_vehicle_visit_flag = [[0 for i in range(_MAX_NUMBER_OF_PASSENGERS)] for j in range(_MAX_NUMBER_OF_VEHICLES)]
# whether vehicle v can take passenger p 1 ok 0 no in prohibit links
# prohibt_visit and passernger can only be carried once control this one
g_vehicle_passenger_visit_allowed_flag = [[0 for i in range(_MAX_NUMBER_OF_VEHICLES)] for j in
                                          range(_MAX_NUMBER_OF_PASSENGERS)]

g_max_vehicle_capacity = 1
g_number_of_passengers = 0

g_outbound_node_id = [[None for i in range(_MAX_NUMBER_OF_NODES)] for j in range(_MAX_NUMBER_OF_OUTBOUND_NODES)]
g_outbound_link_no = [[None for i in range(_MAX_NUMBER_OF_NODES)] for j in range(_MAX_NUMBER_OF_OUTBOUND_NODES)]
g_activity_node_flag = [0] * _MAX_NUMBER_OF_NODES
g_activity_node_ending_time = [99999] * _MAX_NUMBER_OF_NODES
g_activity_node_starting_time = [99999] * _MAX_NUMBER_OF_NODES

g_inbound_node_size = [None] * _MAX_NUMBER_OF_NODES
g_outbound_node_id = [[None for i in range(_MAX_NUMBER_OF_NODES)] for j in range(_MAX_NUMBER_OF_OUTBOUND_NODES)]

g_inbound_node_id = [[None for i in range(_MAX_NUMBER_OF_NODES)] for j in range(_MAX_NUMBER_OF_OUTBOUND_NODES)]
g_inbound_link_no = [[None for i in range(_MAX_NUMBER_OF_NODES)] for j in range(_MAX_NUMBER_OF_OUTBOUND_NODES)]

g_link_free_flow_travel_time = [None] * _MAX_NUMBER_OF_LINKS
g_link_free_flow_travel_time_float_value = [None] * _MAX_NUMBER_OF_LINKS

g_link_link_length = [None] * _MAX_NUMBER_OF_LINKS
g_link_number_of_lanes = [None] * _MAX_NUMBER_OF_LINKS
g_link_mode_code = [None] * _MAX_NUMBER_OF_LINKS
g_link_capacity_per_time_interval = [None] * _MAX_NUMBER_OF_LINKS
g_link_jam_density = [None] * _MAX_NUMBER_OF_LINKS
g_link_service_code = [0] * _MAX_NUMBER_OF_LINKS

g_link_speed = [None] * _MAX_NUMBER_OF_LINKS
g_link_from_node_number = [None] * _MAX_NUMBER_OF_LINKS
g_link_to_node_number = [None] * _MAX_NUMBER_OF_LINKS

g_VOIVTT_per_hour = [None] * _MAX_NUMBER_OF_VEHICLES
g_VOWT_per_hour = [None] * _MAX_NUMBER_OF_VEHICLES

g_vehicle_path_number_of_nodes = [0] * _MAX_NUMBER_OF_VEHICLES

g_vehicle_origin_node = [None] * _MAX_NUMBER_OF_VEHICLES  # for vehcile routings
g_vehicle_destination_node = [None] * _MAX_NUMBER_OF_VEHICLES
g_vehicle_depot_origin_node = [None] * _MAX_NUMBER_OF_VEHICLES  # for vehcile routings
g_vehicle_depot_destination_node = [None] * _MAX_NUMBER_OF_VEHICLES

g_vehicle_departure_time_beginning = [0] * _MAX_NUMBER_OF_VEHICLES
g_vehicle_departure_time_ending = [None] * _MAX_NUMBER_OF_VEHICLES
g_vehicle_arrival_time_beginning = [120] * _MAX_NUMBER_OF_VEHICLES
g_vehicle_arrival_time_ending = [None] * _MAX_NUMBER_OF_VEHICLES

g_passenger_origin_node = [None] * _MAX_NUMBER_OF_PASSENGERS  # traveling passengers
g_passenger_destination_node = [None] * _MAX_NUMBER_OF_PASSENGERS
g_passenger_dummy_destination_node = [-1] * _MAX_NUMBER_OF_PASSENGERS

g_passenger_departure_time_beginning = [None] * _MAX_NUMBER_OF_PASSENGERS
g_passenger_departure_time_ending = [None] * _MAX_NUMBER_OF_PASSENGERS
g_passenger_arrival_time_beginning = [None] * _MAX_NUMBER_OF_PASSENGERS
g_passenger_arrival_time_ending = [None] * _MAX_NUMBER_OF_PASSENGERS

g_vehicle_capacity = [1] * _MAX_NUMBER_OF_VEHICLES

g_number_of_links = 0
g_number_of_nodes = 0
g_number_of_physical_nodes = 0
g_number_of_time_intervals = 10

g_updated_number_of_time_intervals = 0

g_number_of_vehicles = 0

g_number_of_LR_iterations = 1
g_minimum_subgradient_step_size = 0.01

g_shortest_path_debugging_flag = 1
g_waiting_time_ratio = 0.005
g_dummy_vehicle_cost_per_hour = 100

g_travel_time_budget = 100
g_idle_vehicle_benefit = -10

g_activity_node_flag

def g_add_new_node_origin( passenger_id, beginning_time = -1,end_time = -1):

    new_node_number = g_number_of_nodes + 1
    g_outbound_node_size[new_node_number] = 0
    g_inbound_node_size[new_node_number] = 0
    g_node_passenger_id[new_node_number] = passenger_id
    g_activity_node_flag[new_node_number] = 1
    g_activity_node_starting_time[new_node_number] = beginning_time
    g_activity_node_ending_time[new_node_number] = end_time
    g_node_type[new_node_number] = 1

    g_number_of_nodes +=1
    return g_number_of_nodes
