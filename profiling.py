import cProfile
import file_handler

# profiling part
print("Now Profiling is working on add_coffee_module")
cProfile.run('file_handler.add_coffee_module()')

print("Now Profiling is working on new_add_coffee_module")
cProfile.run('file_handler.new_add_coffee_module()')

print("Now Profiling is working on del_coffee_module")
cProfile.run('file_handler.del_coffee_module()')

print("Now Profiling is working on new_del_coffee_module")
cProfile.run('file_handler.new_del_coffee_module()')
