import glob, importlib.util, sys, os
c=sys.argv[1]
for f in sorted(glob.glob(f"books_drafts/{c}_bar*/*.py")):
    s=importlib.util.spec_from_file_location("m",f); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
    print(f"{os.path.basename(f)[:-3]}: {m.BOOK['title']} — " + "; ".join(t for t,_ in m.BOOK['chapters']))
