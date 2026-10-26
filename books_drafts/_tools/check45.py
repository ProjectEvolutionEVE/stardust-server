import glob, importlib.util, sys, os
bad=0; n=0
for f in sorted(glob.glob(sys.argv[1])):
    n+=1
    try:
        s=importlib.util.spec_from_file_location("m",f); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
        B=m.BOOK; t=B["test"]
        assert m.CODE==os.path.basename(f)[:-3], "code"
        assert B["title"] and len(B["chapters"])==6 and len(t)==5, "shape"
        for c in B["chapters"]: assert len(c)==2 and c[1].strip(), "chapter"
        L=set()
        for q,opts,ans in t:
            assert len(opts)==4 and ans in [o[0] for o in opts], (q,ans); L.add(ans)
        assert len(L)>=3, "letters"
    except Exception as e:
        bad+=1; print("BAD",f,e)
print(n,"files",bad,"bad")
