spec ?= packaging/fedora/lunalauncher.spec

.PHONY: srpm

srpm:
	git submodule sync --recursive
	git submodule update --init --recursive
	./packaging/fedora/make-srpm.sh "$(outdir)"
	find "$(outdir)/rpmbuild/SRPMS" -maxdepth 1 -name '*.src.rpm' -exec cp -a {} "$(outdir)/" \;
