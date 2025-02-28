## Kiselev Vasilii resume data (resume.yaml)
### Instructions for running on Ubuntu

. **Install dependencies:**
Open a terminal and run:
DON'T forget about venv
- /Documents$ python -m venv venv
- /Documents$ source venv/bin/activate

```
- sudo apt update
- sudo apt install python3 python3-pip
- pip3 install pyyaml ​​jinja2
```

**Create files:**
- Save `resume.yaml` with your data.
- Save `neobrutalism.html.j2` as a template.
- Save `generate_resume.py` as a script.

**Make the script executable:**
```bash
chmod +x generate_resume.py
```

**Run the script:**
Make sure all files are in the same directory, then run:
```bash
./generate_resume.py
```

**Check the result:**
Open `resume.html` in your browser. You will see a neo-brutalistic resume with rough typography, bright accents, and a minimalist design.
