import os
import sys


pipPath = f'{os.path.dirname(sys.executable)}\\Scripts'
print(os.system(f'setx PATH "%PATH%;{pipPath}"'))