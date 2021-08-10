import agentplus_header as headerconst

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
g_node_passenger_id = [None] * headerconst._MAX_NUMBER_OF_NODES
g_node_type = [None] * headerconst._MAX_NUMBER_OF_NODES  # key nodeid 1: pick up, 2: drop off
g_node_timestamp = [
                       None] * headerconst._MAX_NUMBER_OF_NODES  # key nodeid, values type 1: pick up:ready time, 2: order time
g_node_baseprofit = [None] * headerconst._MAX_NUMBER_OF_NODES  # type 2 = 0
# the number of outbound nodes. key nodeid, values type 1: pick up:ready time, 2: order time
g_outbound_node_size = [None] * headerconst._MAX_NUMBER_OF_NODES
pax_id_to_seq_no_map = {}  # std::map<int, int>

g_passenger_base_profit = [-7] * headerconst._MAX_NUMBER_OF_PASSENGERS
local_vehicle_passenger_additional_profit = [[0 for i in range(headerconst._MAX_NUMBER_OF_VEHICLES)] for j in
                                             range(headerconst._MAX_NUMBER_OF_PASSENGERS)]

g_passenger_order_time = [0] * headerconst._MAX_NUMBER_OF_PASSENGERS
# used in profit(LR multipliers) update: summation of variable y
g_passenger_number_of_visits = [0] * headerconst._MAX_NUMBER_OF_PASSENGERS
g_passenger_vehicle_visit_flag = [[0 for i in range(headerconst._MAX_NUMBER_OF_PASSENGERS)] for j in
                                  range(headerconst._MAX_NUMBER_OF_VEHICLES)]
# whether vehicle v can take passenger p 1 ok 0 no in prohibit links
# prohibt_visit and passernger can only be carried once control this one
g_vehicle_passenger_visit_allowed_flag = [[0 for i in range(headerconst._MAX_NUMBER_OF_VEHICLES)] for j in
                                          range(headerconst._MAX_NUMBER_OF_PASSENGERS)]

g_max_vehicle_capacity = 1
headerconst.g_number_of_passengers = 0

g_outbound_node_id = [[None for i in range(headerconst._MAX_NUMBER_OF_NODES)] for j in
                      range(headerconst._MAX_NUMBER_OF_OUTBOUND_NODES)]
g_outbound_link_no = [[None for i in range(headerconst._MAX_NUMBER_OF_NODES)] for j in
                      range(headerconst._MAX_NUMBER_OF_OUTBOUND_NODES)]
g_activity_node_flag = [0] * headerconst._MAX_NUMBER_OF_NODES
g_activity_node_ending_time = [99999] * headerconst._MAX_NUMBER_OF_NODES
g_activity_node_starting_time = [99999] * headerconst._MAX_NUMBER_OF_NODES

g_inbound_node_size = [None] * headerconst._MAX_NUMBER_OF_NODES
g_outbound_node_id = [[None for i in range(headerconst._MAX_NUMBER_OF_NODES)] for j in
                      range(headerconst._MAX_NUMBER_OF_OUTBOUND_NODES)]

g_inbound_node_id = [[None for i in range(headerconst._MAX_NUMBER_OF_NODES)] for j in
                     range(headerconst._MAX_NUMBER_OF_OUTBOUND_NODES)]
g_inbound_link_no = [[None for i in range(headerconst._MAX_NUMBER_OF_NODES)] for j in
                     range(headerconst._MAX_NUMBER_OF_OUTBOUND_NODES)]

g_link_free_flow_travel_time = [None] * headerconst._MAX_NUMBER_OF_LINKS
g_link_free_flow_travel_time_float_value = [None] * headerconst._MAX_NUMBER_OF_LINKS

g_link_link_length = [None] * headerconst._MAX_NUMBER_OF_LINKS
g_link_number_of_lanes = [None] * headerconst._MAX_NUMBER_OF_LINKS
g_link_mode_code = [None] * headerconst._MAX_NUMBER_OF_LINKS
g_link_capacity_per_time_interval = [None] * headerconst._MAX_NUMBER_OF_LINKS
g_link_jam_density = [None] * headerconst._MAX_NUMBER_OF_LINKS
g_link_service_code = [0] * headerconst._MAX_NUMBER_OF_LINKS

g_link_speed = [None] * headerconst._MAX_NUMBER_OF_LINKS
g_link_from_node_number = [None] * headerconst._MAX_NUMBER_OF_LINKS
g_link_to_node_number = [None] * headerconst._MAX_NUMBER_OF_LINKS

g_VOIVTT_per_hour = [None] * headerconst._MAX_NUMBER_OF_VEHICLES
g_VOWT_per_hour = [None] * headerconst._MAX_NUMBER_OF_VEHICLES

g_vehicle_path_number_of_nodes = [0] * headerconst._MAX_NUMBER_OF_VEHICLES

g_vehicle_origin_node = [None] * headerconst._MAX_NUMBER_OF_VEHICLES  # for vehcile routings
g_vehicle_destination_node = [None] * headerconst._MAX_NUMBER_OF_VEHICLES
g_vehicle_depot_origin_node = [None] * headerconst._MAX_NUMBER_OF_VEHICLES  # for vehcile routings
g_vehicle_depot_destination_node = [None] * headerconst._MAX_NUMBER_OF_VEHICLES

g_vehicle_departure_time_beginning = [0] * headerconst._MAX_NUMBER_OF_VEHICLES
g_vehicle_departure_time_ending = [None] * headerconst._MAX_NUMBER_OF_VEHICLES
g_vehicle_arrival_time_beginning = [120] * headerconst._MAX_NUMBER_OF_VEHICLES
g_vehicle_arrival_time_ending = [None] * headerconst._MAX_NUMBER_OF_VEHICLES

g_passenger_origin_node = [None] * headerconst._MAX_NUMBER_OF_PASSENGERS  # traveling passengers
g_passenger_destination_node = [None] * headerconst._MAX_NUMBER_OF_PASSENGERS
g_passenger_dummy_destination_node = [-1] * headerconst._MAX_NUMBER_OF_PASSENGERS

g_passenger_departure_time_beginning = [None] * headerconst._MAX_NUMBER_OF_PASSENGERS
g_passenger_departure_time_ending = [None] * headerconst._MAX_NUMBER_OF_PASSENGERS
g_passenger_arrival_time_beginning = [None] * headerconst._MAX_NUMBER_OF_PASSENGERS
g_passenger_arrival_time_ending = [None] * headerconst._MAX_NUMBER_OF_PASSENGERS

g_vehicle_capacity = [1] * headerconst._MAX_NUMBER_OF_VEHICLES

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

#g_activity_node_flag


def g_add_new_node_origin(passenger_id, beginning_time=-1, end_time=-1):
    global g_number_of_nodes
    new_node_number = g_number_of_nodes + 1
    g_outbound_node_size[new_node_number] = 0
    g_inbound_node_size[new_node_number] = 0
    g_node_passenger_id[new_node_number] = passenger_id
    g_activity_node_flag[new_node_number] = 1
    g_activity_node_starting_time[new_node_number] = beginning_time
    g_activity_node_ending_time[new_node_number] = end_time
    g_node_type[new_node_number] = 1

    g_number_of_nodes += 1
    return g_number_of_nodes

def fprintf(stream, format_spec, *args):
    stream.write(format_spec % args)

def g_add_new_node(vehicle_id, beginning_time = -1, end_time = -1):

    new_node_number = g_number_of_nodes + 1
    g_outbound_node_size[new_node_number] = 0
    g_inbound_node_size[new_node_number] = 0
    g_node_passenger_id[new_node_number] = 0
    g_activity_node_flag[new_node_number] = 1
    g_activity_node_starting_time[new_node_number] = beginning_time
    g_activity_node_ending_time[new_node_number] = end_time
    g_node_type[new_node_number] = 3
    g_number_of_nodes += 1
    return g_number_of_nodes

def g_add_new_node_destination(passenger_id, beginning_time = -1, end_time = -1):

    new_node_number = g_number_of_nodes + 1
    g_outbound_node_size[new_node_number] = 0
    g_inbound_node_size[new_node_number] = 0
    g_node_passenger_id[new_node_number] = passenger_id
    g_activity_node_flag[new_node_number] = 1
    g_activity_node_starting_time[new_node_number] = beginning_time
    g_activity_node_ending_time[new_node_number] = end_time
    g_node_type[new_node_number] = 2
    g_number_of_nodes+=1
    return g_number_of_nodes

def g_add_new_link(from_node_id, to_node_id, passenger_id = 0, travel_time = 1, link_length = 1, number_of_lanes = 1, mode_code = 0, capacity_per_time_interval = 1,speed = 60):
    global g_number_of_links
    new_link_id = g_number_of_links
    g_outbound_node_id[from_node_id][g_outbound_node_size[from_node_id]] = to_node_id
    g_outbound_link_no[from_node_id][g_outbound_node_size[from_node_id]] = new_link_id

    g_outbound_node_size[from_node_id]+=1

    g_inbound_node_id[to_node_id][g_inbound_node_size[to_node_id]] = from_node_id
    g_inbound_link_no[to_node_id][g_inbound_node_size[to_node_id]] = new_link_id
    g_inbound_node_size[to_node_id]+=1


    g_link_from_node_number[new_link_id] = from_node_id
    g_link_to_node_number[new_link_id] = to_node_id

    g_link_free_flow_travel_time[new_link_id] = max(1, travel_time)

    g_link_link_length[g_number_of_links] = link_length
    g_link_number_of_lanes[g_number_of_links] = number_of_lanes
    g_link_mode_code[g_number_of_links] = mode_code
    g_link_capacity_per_time_interval[g_number_of_links] = capacity_per_time_interval
    g_link_speed[g_number_of_links] = speed
    g_link_service_code[g_number_of_links] = passenger_id

    g_number_of_links+=1
    return g_number_of_links


# class for vehicle scheduling states



class CVSState:
    current_node_id = None  # space dimension
    # passengerID, nodeType
    passenger_service_state = {}
    passenger_service_time = {}
    passenger_service_begin_time = {}


    passenger_carrying_state = {}
# visit nodes
    m_visit_sequence = []  # store nodes f
    m_visit_time_sequence = []  # store passing nodes times

    m_vehicle_capacity = None  # int
    LabelCost = None  # with LR price (float)
    PrimalLabelCost = None  # without LR price(float)
    m_final_arrival_time = None  # for ending states(int)


    # CONSTRUCTOR CVSSTATE()
    def __init__(self, m_final_arrival_time, LabelCost, m_vehicle_capacity):
        m_final_arrival_time = 0


    LabelCost = headerconst._MAX_LABEL_COST
    m_vehicle_capacity = 0


    def Copy(pSource):
        current_node_id = pSource.current_node_id
        global passenger_service_state
        global passenger_service_time
        global passenger_service_begin_time
        global passenger_carrying_state
        global m_visit_sequence
        global m_visit_time_sequence

        passenger_service_state.clear()
        passenger_service_state = pSource.passenger_service_state

        passenger_service_time.clear()
        passenger_service_time = pSource.passenger_service_time

        passenger_service_begin_time.clear()
        passenger_service_begin_time = pSource.passenger_service_begin_time

        passenger_carrying_state.clear()
        passenger_carrying_state = pSource.passenger_carrying_state

        m_visit_sequence.clear()
        m_visit_sequence = pSource.m_visit_sequence
        m_visit_time_sequence.clear()
        m_visit_time_sequence = pSource.m_visit_time_sequence
        m_vehicle_capacity = pSource.m_vehicle_capacity
        LabelCost = pSource.LabelCost


    def GetPassengerServiceState(passenger_id):
        # value != last item of dictionary
        if passenger_service_state.get(passenger_id) != list(passenger_service_state.values())[-1]:
            return passenger_service_state[passenger_id]  # 1 or 2


        return 0


    def StartCarryingService(passenger_id, service_time):
        global m_vehicle_capacity
        passenger_carrying_state[passenger_id] = 1
        m_vehicle_capacity += 1

        passenger_service_begin_time[passenger_id] = service_time


    def CompleteCarryingService(passenger_id, service_time):


        iter = passenger_carrying_state.get(passenger_id)
        if iter != list(passenger_carrying_state.values())[-1]:
            passenger_carrying_state.pop(passenger_id)
            m_vehicle_capacity -= 1

        passenger_service_time[passenger_id] = service_time


    # Start or Complete service
    def MarkCarryingService(passenger_id, node_type, ServiceTime):
        if node_type == 1:
            CVSState.StartCarryingService(passenger_id, ServiceTime)
        elif node_type == 2:
            CVSState.CompleteCarryingService(passenger_id, ServiceTime)


    def IsAllServiceComplete(self):
        if len(passenger_carrying_state) == 0:
            return True


        return False


    # state actually node in SP. label cost
    def CalculateLabelCost(vehicle_id):
        LabelCost = 0
        PrimalLabelCost = 0
        i = 0


        iterator = list(passenger_service_state.items())
        for num in iterator:
            if num[1] == 2:
                i += 1
                passenger_id = num[0]
                LabelCost -= g_passenger_base_profit[passenger_id]  # LBd

            # the waiting cost of passenger is 0.3
                LabelCost += 0.3 * max(0, (passenger_service_begin_time[passenger_id] - g_passenger_order_time[passenger_id]))
                PrimalLabelCost += 0.3 * max(0, (
                        passenger_service_begin_time[passenger_id] - g_passenger_order_time[passenger_id]))

    # total travel time
            LabelCost += m_visit_time_sequence[m_visit_time_sequence.size() - 1] - g_vehicle_departure_time_beginning[1]
            PrimalLabelCost += m_visit_time_sequence[m_visit_time_sequence.size() - 1] - g_vehicle_departure_time_beginning[1]

    # the difference between waiting cost and transportation cost
            keys = list(m_visit_sequence.keys())
            for num in m_visit_sequence:
                it = 1
                if m_visit_sequence[keys[it - 1]] == m_visit_sequence[keys[it]]:  # waiting arc
                    LabelCost -= (1 - 0.5) * (m_visit_time_sequence[keys[it]] - m_visit_time_sequence[keys[it - 1]])  # cost of waiting arc is 0.5
                    PrimalLabelCost -= (1 - 0.5) * (m_visit_time_sequence[keys[it]] - m_visit_time_sequence[keys[it - 1]])


    # class CVSState  record pax and vehicle's completed service
    def CountPassengerNumberOfVisits(vehicle_id):
        iterator = list(passenger_service_state.items())


        for num in iterator:
            if num[1] == 2:  # complete
                passenger_id = num[0]
            # pragma omp critical

                g_passenger_number_of_visits[passenger_id] += 1
                g_passenger_vehicle_visit_flag[passenger_id][vehicle_id] = 1




        def generate_string_key():
            global current_node_id
            s = "n"
            s += str(current_node_id)  # space key


            iterator = list(passenger_service_state.items())
            for values in iterator:
                s += "_"

                s += str(values[0]) + "[" + str(values[1]) + "]"

            return s


class C_time_indexed_state_vector:
    current_time = None

    m_VSStateVector = []  # CVSState vector
    # state string 1_1_1,state index
    m_state_map = {}

    def Reset(self):
        current_time = 0

    m_VSStateVector.clear()
    m_state_map.clear()

    def m_find_state_index(string_key):
        if C_time_indexed_state_vector.m_state_map[string_key]:
            return C_time_indexed_state_vector.m_state_map[string_key]
        else:
            return -1  # not found

    def update_state(new_element):
        new_element = CVSState()
        global LabelCost

        string_key = new_element.generate_string_key()  # if it is new, string is n100, no state index
        state_index = C_time_indexed_state_vector.m_find_state_index(string_key)

        if state_index == -1:  # no such state at this time

        # add new state
        state_index = C_time_indexed_state_vector.m_VSStateVector.len()
        C_time_indexed_state_vector.m_VSStateVector.append(new_element)
        C_time_indexed_state_vector.m_state_map[string_key] = state_index

        #elif new_element.LabelCost < C_time_indexed_state_vector.m_VSStateVector[state_index].LabelCost:


            #C_time_indexed_state_vector.m_VSStateVector[state_index].Copy(new_element)


    def Sort(self):
        C_time_indexed_state_vector.m_VSStateVector.sort()
        C_time_indexed_state_vector.m_state_map.clear()  # invalid


    def SortAndCleanEndingState(BestKValue):
        if C_time_indexed_state_vector.m_VSStateVector.len() > 2 * BestKValue:
            C_time_indexed_state_vector.m_VSStateVector.sort()

            C_time_indexed_state_vector.m_state_map.clear()  # invalid


        for values in C_time_indexed_state_vector.m_VSStateVector:
            if C_time_indexed_state_vector.m_VSStateVector.index(values) >= BestKValue:
                C_time_indexed_state_vector.m_VSStateVector.remove(values)


    def GetBestValue(DualPriceFlag, vehicle_id):


        # LabelCost not PrimalCost when sorting
        C_time_indexed_state_vector.m_VSStateVector.sort()
        if C_time_indexed_state_vector.m_VSStateVector.len() >= 1:

            state_str = C_time_indexed_state_vector.m_VSStateVector[0].generate_string_key()
            # 0 means least cost
            C_time_indexed_state_vector.m_VSStateVector[0].CountPassengerNumberOfVisits(vehicle_id)
            if DualPriceFlag == 1:

                fprintf(g_pFileDebugLog, "Dual \t{{%s}} Label Cost %f\n ", state_str.c_str(), C_time_indexed_state_vector.m_VSStateVector[0].LabelCost)

            else:
                fprintf(g_pFileDebugLog, "Primal \t{{%s}} Label Cost %f\n", state_str.c_str(),
                        C_time_indexed_state_vector.m_VSStateVector[0].PrimalLabelCost)

            if DualPriceFlag == 1:
                return C_time_indexed_state_vector.m_VSStateVector[0].LabelCost
            else:
                return C_time_indexed_state_vector.m_VSStateVector[0].PrimalLabelCost

        else:
            return headerconst._MAX_LABEL_COST


