spec ?= packaging/fedora/lunalauncher.spec

.PHONY: srpm

srpm:
	LUNALAUNCHER_SRPM_SOURCE_MODE=worktree ./packaging/fedora/make-srpm.sh "$(outdir)"
	find "$(outdir)/rpmbuild/SRPMS" -maxdepth 1 -name '*.src.rpm' -exec cp -a {} "$(outdir)/" \;
