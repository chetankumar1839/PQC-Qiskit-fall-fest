from backend.pqc_wrapper import PQCWrapper

wrapper = PQCWrapper()

print("30% RISK:")
print(wrapper.respond(0.30))

print("\n40% RISK:")
print(wrapper.respond(0.40))

print("\n67.97% RISK:")
print(wrapper.respond(0.6797))