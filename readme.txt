1. I started the first python script, Just have some questions to clarify with prof and slack channel.

2. When using slack I often recieve the following error: 

for example

% time spack spec zlib                                                   
==> Bootstrapping clingo from pre-built binaries
==> Bootstrapping clingo from sources
==> Installing libiconv-1.16-zmllitveoyqsjft72ejnnczciytx7wam
==> No binary for libiconv-1.16-zmllitveoyqsjft72ejnnczciytx7wam found: installing from source
==> Error: FetchError: All fetchers failed for spack-stage-libiconv-1.16-zmllitveoyqsjft72ejnnczciytx7wam

/Users/majed/spack/lib/spack/spack/package_base.py:1550, in do_fetch:
       1547
       1548        self.stage.create()
       1549        err_msg = None if not self.manual_download else self.download_instr
  >>   1550        start_time = time.time()
       1551        self.stage.fetch(mirror_only, err_msg=err_msg)
       1552        self._fetch_time = time.time() - start_time
       1553


==> Warning: Skipping build of diffutils-3.8-uswlxudolvoac3jzgki47zapwnlkdfux since libiconv-1.16-zmllitveoyqsjft72ejnnczciytx7wam failed
==> Warning: Skipping build of bzip2-1.0.8-bmhr6xblrfrjdqtm6dzgb6gf443ig3br since diffutils-3.8-uswlxudolvoac3jzgki47zapwnlkdfux failed
==> Warning: Skipping build of perl-5.34.1-z4z5s7hgbvwdioavvu363fieh4mvwixl since bzip2-1.0.8-bmhr6xblrfrjdqtm6dzgb6gf443ig3br failed
==> Warning: Skipping build of bison-3.8.2-6vj5yg3w5mcghoai6edgrl2ju4vnpaje since perl-5.34.1-z4z5s7hgbvwdioavvu363fieh4mvwixl failed
==> Warning: Skipping build of clingo-bootstrap-spack-cduds7mv2xqnbza56m647ajhdc2qaqdk since bison-3.8.2-6vj5yg3w5mcghoai6edgrl2ju4vnpaje failed
==> Warning: Skipping build of openssl-1.1.1o-yn4eulkpdj73xla4lpddu4ozreey2jjy since perl-5.34.1-z4z5s7hgbvwdioavvu363fieh4mvwixl failed
==> Warning: Skipping build of cmake-3.23.2-72osugp7rlxotg6nom4jidb6xlnv2ljs since openssl-1.1.1o-yn4eulkpdj73xla4lpddu4ozreey2jjy failed
==> Error: cannot bootstrap the "clingo" Python module from spec "clingo-bootstrap@spack+python %apple-clang target=x86_64" due to the following failures:
github-actions-v0.2 raised RuntimeError: The binary index is empty
github-actions-v0.1 raised ValueError: source is not trusted
spack-install raised InstallError: Terminating after first install failure: FetchError: All fetchers failed for spack-stage-libiconv-1.16-zmllitveoyqsjft72ejnnczciytx7wam
Run `spack --debug ...` for more detailed errors

I need to resolve this error to be able to meaningfully test my script.
