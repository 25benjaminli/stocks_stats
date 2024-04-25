Hi...

To run the program, first install requirements.txt

If you encounter any dependency issues, here is how to debug:
1. Make sure python version is 3.8
2. If it gives error during setuptools installation, ensure that setuptools is setuptools==57.5.0
3. Install torch with GPU if that's what you intend to run it with
4. Tensorflow.. is a prerequisite for a dependency but seems to cause some issues. Maybe this will be resolved at a later date. 