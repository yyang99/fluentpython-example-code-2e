# tag::REGISTRATION_PARAM[]

from registration_param_2_module_registry import registry
import registration_param_2_module_funcs    # Note: need this import to register funcs in registration_param_2_module_funcs.py

# end::REGISTRATION_PARAM[]
if __name__ == "__main__":
    print(registry)
