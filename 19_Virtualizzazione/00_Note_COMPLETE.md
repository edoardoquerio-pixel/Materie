# Virtualizzazione — Quaderno di Appunti

> **Materia:** 19_Virtualizzazione
> **Data generazione:** Febbraio 2026
> **Corso:** ITS ICT Cloud Specialist 2025-2027

---

## Indice delle Sessioni

1. [123 CHANGELOG](#123-changelog)
2. [125 README](#125-readme)
3. [129 main](#129-main)
4. [134 README](#134-readme)
5. [main](#main)
6. [docker-compose](#docker-compose)
7. [list](#list)
8. [README](#readme)
9. [CHANGELOG](#changelog)
10. [README](#readme)
11. [db](#db)
12. [package](#package)
13. [server](#server)
14. [README](#readme)
15. [db](#db)
16. [package](#package)
17. [server](#server)
18. [db](#db)
19. [package](#package)
20. [server](#server)
21. [VirtCSP - Scheda 1 - Openstack](#virtcsp---scheda-1---openstack)
22. [Virtualizzazione 26 - Infrastruttura virtuale](#virtualizzazione-26---infrastruttura-virtuale)
23. [Virtualizzazione 26 - La Virtualizzazione di Mem](#virtualizzazione-26---la-virtualizzazione-di-mem)
24. [Virtualizzazione 26 - La Virtualizzazione di Networking](#virtualizzazione-26---la-virtualizzazione-di-networking)
25. [Virtualizzazione 26 - La Virtualizzazione](#virtualizzazione-26---la-virtualizzazione)
26. [Virtualizzazione 26 - VM e Openstack](#virtualizzazione-26---vm-e-openstack)

---

# CHANGELOG

**File:** `CHANGELOG.md`
**Tipo:** `.md`
**Dimensione:** 34.5 KB
**Ultima modifica:** 15/06/2026 12:48

---


<a name="v3.9.0"></a>
## [v3.9.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.8.0...v3.9.0) (2025-11-09)

### Chore

* Add file requested by hashicorp ([#813](https://github.com/kreuzwerker/terraform-provider-docker/issues/813))
* Prepare release v3.8.0 ([#806](https://github.com/kreuzwerker/terraform-provider-docker/issues/806))

### Feat

* Implement caching of docker provider ([#808](https://github.com/kreuzwerker/terraform-provider-docker/issues/808))

### Fix

* test attribute of docker_service healthcheck is not required ([#815](https://github.com/kreuzwerker/terraform-provider-docker/issues/815))
* docker_service label can be updated without recreate ([#814](https://github.com/kreuzwerker/terraform-provider-docker/issues/814))


<a name="v3.8.0"></a>
## [v3.8.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.7.0...v3.8.0) (2025-10-08)

### Feat

* Add build attribute for docker_registry_image ([#805](https://github.com/kreuzwerker/terraform-provider-docker/issues/805))
* Add build option for additional contexts ([#798](https://github.com/kreuzwerker/terraform-provider-docker/issues/798))
* implement mac_address for networks_advanced ([#794](https://github.com/kreuzwerker/terraform-provider-docker/issues/794))
* Implement docker cluster volume ([#793](https://github.com/kreuzwerker/terraform-provider-docker/issues/793))


<a name="v3.7.0"></a>
## [v3.7.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.6.2...v3.7.0) (2025-08-19)

### Chore

* Prepare release v3.7.0 ([#774](https://github.com/kreuzwerker/terraform-provider-docker/issues/774))

### Feat

* Implement memory_reservation and network_mode enhancements ([#773](https://github.com/kreuzwerker/terraform-provider-docker/issues/773))
* Implement cache_from and cache_to for docker_image ([#772](https://github.com/kreuzwerker/terraform-provider-docker/issues/772))

### Fix

* Correctly get and set nanoCPUs for docker_container ([#771](https://github.com/kreuzwerker/terraform-provider-docker/issues/771))


<a name="v3.6.2"></a>
## [v3.6.2](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.6.1...v3.6.2) (2025-06-13)

### Chore

* Prepare release v3.6.2 ([#750](https://github.com/kreuzwerker/terraform-provider-docker/issues/750))

### Feat

* Allow digest in image name ([#744](https://github.com/kreuzwerker/terraform-provider-docker/issues/744))

### Fix

* Remove wrong buildkit version assignment ([#747](https://github.com/kreuzwerker/terraform-provider-docker/issues/747))
* Reading non existant volume should recreate ([#749](https://github.com/kreuzwerker/terraform-provider-docker/issues/749))
* Typo in cgroup_parent handling ([#746](https://github.com/kreuzwerker/terraform-provider-docker/issues/746))


<a name="v3.6.1"></a>
## [v3.6.1](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.6.0...v3.6.1) (2025-06-05)

### Chore

* Prepare release v3.6.1 ([#743](https://github.com/kreuzwerker/terraform-provider-docker/issues/743))

### Feat

* allow to set the cgroup parent for container ([#609](https://github.com/kreuzwerker/terraform-provider-docker/issues/609))


<a name="v3.6.0"></a>
## [v3.6.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.5.0...v3.6.0) (2025-05-25)

### Chore

* Prepare release v3.6.0 ([#735](https://github.com/kreuzwerker/terraform-provider-docker/issues/735))

### Feat

* Implement correct cpu scheduler settings ([#732](https://github.com/kreuzwerker/terraform-provider-docker/issues/732))
* Add implementaion of capabilities in docker servic ([#727](https://github.com/kreuzwerker/terraform-provider-docker/issues/727))
* implement Buildx builder resource ([#724](https://github.com/kreuzwerker/terraform-provider-docker/issues/724))

### Fix

* Implement buildx fixes for general buildkit support and platform handling ([#734](https://github.com/kreuzwerker/terraform-provider-docker/issues/734))
* Make endpoint validation less strict ([#733](https://github.com/kreuzwerker/terraform-provider-docker/issues/733))


<a name="v3.5.0"></a>
## [v3.5.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.4.0...v3.5.0) (2025-05-06)

### Chore

* Prepare release v3.5.0 ([#721](https://github.com/kreuzwerker/terraform-provider-docker/issues/721))

### Feat

* Implement using of buildx for docker_image ([#717](https://github.com/kreuzwerker/terraform-provider-docker/issues/717))
* Support registries that return empty auth scope [#646](https://github.com/kreuzwerker/terraform-provider-docker/issues/646)
* Implement registry_image_manifests data source ([#714](https://github.com/kreuzwerker/terraform-provider-docker/issues/714))
* Implement healthcheck start interval ([#713](https://github.com/kreuzwerker/terraform-provider-docker/issues/713))


<a name="v3.4.0"></a>
## [v3.4.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.3.0...v3.4.0) (2025-04-25)

### Chore

* Prepare release v3.4.0 ([#712](https://github.com/kreuzwerker/terraform-provider-docker/issues/712))

### Feat

* Implement volume_options subpath ([#710](https://github.com/kreuzwerker/terraform-provider-docker/issues/710))

### Fix

* Prevent recreation of image name is intentionally set to a fixed value ([#711](https://github.com/kreuzwerker/terraform-provider-docker/issues/711))
* Improve container wait handling ([#709](https://github.com/kreuzwerker/terraform-provider-docker/issues/709))
* Use auth_config block also for registry_image delete functionality ([#708](https://github.com/kreuzwerker/terraform-provider-docker/issues/708))


<a name="v3.3.0"></a>
## [v3.3.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.2.0...v3.3.0) (2025-04-19)

### Chore

* Prepare release v3.3.0 ([#705](https://github.com/kreuzwerker/terraform-provider-docker/issues/705))
* Update terraform-plugin-sdk/v2 dependency ([#699](https://github.com/kreuzwerker/terraform-provider-docker/issues/699))
* Update docker/docker and docker/cli to newest stable ([#695](https://github.com/kreuzwerker/terraform-provider-docker/issues/695))

### Feat

* Implement support for docker context ([#704](https://github.com/kreuzwerker/terraform-provider-docker/issues/704))
* disable_docker_daemon_check for provider ([#703](https://github.com/kreuzwerker/terraform-provider-docker/issues/703))
* Implement tag triggers for docker_tag resource ([#702](https://github.com/kreuzwerker/terraform-provider-docker/issues/702))
* Implement auth_config for docker_registry_image ([#701](https://github.com/kreuzwerker/terraform-provider-docker/issues/701))

### Fix

* Store correctly ports from server ([#698](https://github.com/kreuzwerker/terraform-provider-docker/issues/698))


<a name="v3.2.0"></a>
## [v3.2.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.1.2...v3.2.0) (2025-04-16)

### Chore

* Prepare release v3.2.0 ([#694](https://github.com/kreuzwerker/terraform-provider-docker/issues/694))
* Upgrade golangci-lint to next major version ([#686](https://github.com/kreuzwerker/terraform-provider-docker/issues/686))

### Docs

* Consolidated update of docs from several PRs ([#691](https://github.com/kreuzwerker/terraform-provider-docker/issues/691))

### Feat

* Implement upload permissions in docker_container resource ([#693](https://github.com/kreuzwerker/terraform-provider-docker/issues/693))
* Implement docker_image timeouts ([#692](https://github.com/kreuzwerker/terraform-provider-docker/issues/692))
* Add support for build-secrets ([#604](https://github.com/kreuzwerker/terraform-provider-docker/issues/604))

### Fix

* Authentication to ECR public ([#690](https://github.com/kreuzwerker/terraform-provider-docker/issues/690))


<a name="v3.1.2"></a>
## [v3.1.2](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.1.1...v3.1.2) (2025-04-15)

### Chore

* prepare release 3.1.2 ([#688](https://github.com/kreuzwerker/terraform-provider-docker/issues/688))


<a name="v3.1.1"></a>
## [v3.1.1](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.1.0...v3.1.1) (2025-04-14)

### Chore

* Prepare release 3.1.1 ([#687](https://github.com/kreuzwerker/terraform-provider-docker/issues/687))


<a name="v3.1.0"></a>
## [v3.1.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.0.2...v3.1.0) (2025-04-14)

### Chore

* Prepare release 3.1.0 ([#685](https://github.com/kreuzwerker/terraform-provider-docker/issues/685))
* update Go version to 1.22 for consistency across workflows, jo… ([#613](https://github.com/kreuzwerker/terraform-provider-docker/issues/613))

### Feat

* support setting cpu shares ([#575](https://github.com/kreuzwerker/terraform-provider-docker/issues/575))

### Fix

* Use build_args everywhere and update documentation ([#681](https://github.com/kreuzwerker/terraform-provider-docker/issues/681))
* Compress build context before sending it to Docker ([#461](https://github.com/kreuzwerker/terraform-provider-docker/issues/461))
* Set correct default network driver and fix a test ([#677](https://github.com/kreuzwerker/terraform-provider-docker/issues/677))

### Typo

* s/presend/present/ ([#606](https://github.com/kreuzwerker/terraform-provider-docker/issues/606))


<a name="v3.0.2"></a>
## [v3.0.2](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.0.1...v3.0.2) (2023-03-17)

### Chore

* Prepare release v3.0.2

### Docs

* correct spelling of "networks_advanced" ([#517](https://github.com/kreuzwerker/terraform-provider-docker/issues/517))

### Fix

* Implement proxy support. ([#529](https://github.com/kreuzwerker/terraform-provider-docker/issues/529))


<a name="v3.0.1"></a>
## [v3.0.1](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.0.0...v3.0.1) (2023-01-13)

### Chore

* Prepare release v3.0.1

### Fix

* Access health of container correctly. ([#506](https://github.com/kreuzwerker/terraform-provider-docker/issues/506))


<a name="v3.0.0"></a>
## [v3.0.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.25.0...v3.0.0) (2023-01-13)

### Chore

* Prepare release v3.0.0

### Docs

* Update documentation.
* Add migration guide and update README ([#502](https://github.com/kreuzwerker/terraform-provider-docker/issues/502))

### Feat

* Prepare v3 release ([#503](https://github.com/kreuzwerker/terraform-provider-docker/issues/503))


<a name="v2.25.0"></a>
## [v2.25.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.24.0...v2.25.0) (2023-01-05)

### Chore

* Prepare release v2.25.0

### Docs

* Add documentation of remote hosts. ([#498](https://github.com/kreuzwerker/terraform-provider-docker/issues/498))

### Feat

* Migrate build block to `docker_image` ([#501](https://github.com/kreuzwerker/terraform-provider-docker/issues/501))
* Add platform attribute to docker_image resource ([#500](https://github.com/kreuzwerker/terraform-provider-docker/issues/500))
* Add sysctl implementation to container of docker_service. ([#499](https://github.com/kreuzwerker/terraform-provider-docker/issues/499))


<a name="v2.24.0"></a>
## [v2.24.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.23.1...v2.24.0) (2022-12-23)

### Chore

* Prepare release v2.24.0

### Docs

* Fix generated website.
* Update command typo ([#487](https://github.com/kreuzwerker/terraform-provider-docker/issues/487))

### Feat

* cgroupns support ([#497](https://github.com/kreuzwerker/terraform-provider-docker/issues/497))
* Add triggers attribute to docker_registry_image ([#496](https://github.com/kreuzwerker/terraform-provider-docker/issues/496))
* Support registries with disabled auth ([#494](https://github.com/kreuzwerker/terraform-provider-docker/issues/494))
* add IPAM options block for docker networks ([#491](https://github.com/kreuzwerker/terraform-provider-docker/issues/491))

### Fix

* Pin data source specific tag test to older tag.

### Tests

* Add test for parsing auth headers.


<a name="v2.23.1"></a>
## [v2.23.1](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.23.0...v2.23.1) (2022-11-23)

### Chore

* Prepare release v2.23.1

### Fix

* Update shasum of busybox:1.35.0 tag in test.
* Handle Auth Header Scopes ([#482](https://github.com/kreuzwerker/terraform-provider-docker/issues/482))
* Set OS_ARCH from GOHOSTOS and GOHOSTARCH ([#477](https://github.com/kreuzwerker/terraform-provider-docker/issues/477))


<a name="v2.23.0"></a>
## [v2.23.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.22.0...v2.23.0) (2022-11-02)

### Chore

* Prepare release v2.23.0

### Feat

* wait container healthy state ([#467](https://github.com/kreuzwerker/terraform-provider-docker/issues/467))
* add docker logs data source ([#471](https://github.com/kreuzwerker/terraform-provider-docker/issues/471))

### Fix

* Update shasum of busybox:1.35.0 tag in test.
* Update shasum of busybox:1.35.0 tag
* Correct provider name to match the public registry ([#462](https://github.com/kreuzwerker/terraform-provider-docker/issues/462))


<a name="v2.22.0"></a>
## [v2.22.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.21.0...v2.22.0) (2022-09-20)

### Chore

* Prepare release v2.22.0

### Feat

* Configurable timeout for docker_container resource stateChangeConf ([#454](https://github.com/kreuzwerker/terraform-provider-docker/issues/454))

### Fix

* oauth authorization support for azurecr ([#451](https://github.com/kreuzwerker/terraform-provider-docker/issues/451))


<a name="v2.21.0"></a>
## [v2.21.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.20.3...v2.21.0) (2022-09-05)

### Chore

* Prepare release v2.21.0

### Docs

* Fix docker config example.

### Feat

* Add image_id attribute to docker_image resource. ([#450](https://github.com/kreuzwerker/terraform-provider-docker/issues/450))
* Update used goversion to 1.18. ([#449](https://github.com/kreuzwerker/terraform-provider-docker/issues/449))

### Fix

* Replace deprecated .latest attribute with new image_id. ([#453](https://github.com/kreuzwerker/terraform-provider-docker/issues/453))
* Remove reading part of docker_tag resource. ([#448](https://github.com/kreuzwerker/terraform-provider-docker/issues/448))
* Fix repo_digest value for DockerImageDatasource test.


<a name="v2.20.3"></a>
## [v2.20.3](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.20.2...v2.20.3) (2022-08-31)

### Chore

* Prepare release v2.20.3

### Fix

* Docker Registry Image data source use HEAD request to query image digest ([#433](https://github.com/kreuzwerker/terraform-provider-docker/issues/433))
* Adding Support for Windows Paths in Bash ([#438](https://github.com/kreuzwerker/terraform-provider-docker/issues/438))


<a name="v2.20.2"></a>
## [v2.20.2](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.20.1...v2.20.2) (2022-08-10)

### Chore

* Prepare release v2.20.2

### Fix

* Check the operating system for determining the default Docker socket ([#427](https://github.com/kreuzwerker/terraform-provider-docker/issues/427))

### Reverts

* fix(deps): update module github.com/golangci/golangci-lint to v1.48.0 ([#423](https://github.com/kreuzwerker/terraform-provider-docker/issues/423))


<a name="v2.20.1"></a>
## [v2.20.1](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.20.0...v2.20.1) (2022-08-10)

### Chore

* Prepare release v2.20.1
* Reduce time to setup AccTests ([#430](https://github.com/kreuzwerker/terraform-provider-docker/issues/430))

### Docs

* Improve docker network usage documentation [skip-ci]

### Feat

* Implement triggers attribute for docker_image. ([#425](https://github.com/kreuzwerker/terraform-provider-docker/issues/425))

### Fix

* Add ForceTrue to docker_image name attribute. ([#421](https://github.com/kreuzwerker/terraform-provider-docker/issues/421))


<a name="v2.20.0"></a>
## [v2.20.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.19.0...v2.20.0) (2022-07-28)

### Chore

* Prepare release v2.20.0
* Fix release targets in Makefile.

### Feat

* Implementation of `docker_tag` resource. ([#418](https://github.com/kreuzwerker/terraform-provider-docker/issues/418))
* Implement support for insecure registries ([#414](https://github.com/kreuzwerker/terraform-provider-docker/issues/414))


<a name="v2.19.0"></a>
## [v2.19.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.18.1...v2.19.0) (2022-07-15)

### Chore

* Prepare release v2.19.0

### Feat

* Add gpu flag to docker_container resource ([#405](https://github.com/kreuzwerker/terraform-provider-docker/issues/405))

### Fix

* Enable authentication to multiple registries again. ([#400](https://github.com/kreuzwerker/terraform-provider-docker/issues/400))
* ECR authentication ([#409](https://github.com/kreuzwerker/terraform-provider-docker/issues/409))


<a name="v2.18.1"></a>
## [v2.18.1](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.18.0...v2.18.1) (2022-07-14)

### Chore

* Prepare release v2.18.1
* Automate changelog generation [skip ci]

### Fix

* Improve searchLocalImages error handling. ([#407](https://github.com/kreuzwerker/terraform-provider-docker/issues/407))
* Throw errors when any part of docker config file handling goes wrong. ([#406](https://github.com/kreuzwerker/terraform-provider-docker/issues/406))
* Enables having a Dockerfile outside the context ([#402](https://github.com/kreuzwerker/terraform-provider-docker/issues/402))


<a name="v2.18.0"></a>
## [v2.18.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.17.0...v2.18.0) (2022-07-11)

### Chore

* prepare release v2.18.0

### Feat

* add runtime, stop_signal and stop_timeout properties to the docker_container resource ([#364](https://github.com/kreuzwerker/terraform-provider-docker/issues/364))

### Fix

* Correctly handle build files and context for docker_registry_image ([#398](https://github.com/kreuzwerker/terraform-provider-docker/issues/398))
* Switch to proper go tools mechanism to fix website-* workflows. ([#399](https://github.com/kreuzwerker/terraform-provider-docker/issues/399))
* compare relative paths when excluding, fixes kreuzwerker[#280](https://github.com/kreuzwerker/terraform-provider-docker/issues/280) ([#397](https://github.com/kreuzwerker/terraform-provider-docker/issues/397))


<a name="v2.17.0"></a>
## [v2.17.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.16.0...v2.17.0) (2022-06-23)

### Chore

* prepare release v2.17.0
* Exclude examples directory from renovate.
* remove the workflow to close stale issues and pull requests ([#371](https://github.com/kreuzwerker/terraform-provider-docker/issues/371))

### Fix

* update go package files directly on master to fix build.
* correct authentication for ghcr.io registry([#349](https://github.com/kreuzwerker/terraform-provider-docker/issues/349))


<a name="v2.16.0"></a>
## [v2.16.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.15.0...v2.16.0) (2022-01-24)

### Chore

* prepare release v2.16.0

### Docs

* fix service options ([#337](https://github.com/kreuzwerker/terraform-provider-docker/issues/337))
* update registry_image.md ([#321](https://github.com/kreuzwerker/terraform-provider-docker/issues/321))
* fix r/registry_image truncated docs ([#304](https://github.com/kreuzwerker/terraform-provider-docker/issues/304))

### Feat

* add parameter for SSH options ([#335](https://github.com/kreuzwerker/terraform-provider-docker/issues/335))

### Fix

* pass container rm flag ([#322](https://github.com/kreuzwerker/terraform-provider-docker/issues/322))
* add nil check of DriverConfig ([#315](https://github.com/kreuzwerker/terraform-provider-docker/issues/315))
* fmt of go files for go 1.17


<a name="v2.15.0"></a>
## [v2.15.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.14.0...v2.15.0) (2021-08-11)

### Chore

* prepare release v2.15.0
* re go gets terraform-plugin-docs

### Docs

* corrects authentication misspell. Closes [#264](https://github.com/kreuzwerker/terraform-provider-docker/issues/264)

### Feat

* add container storage opts ([#258](https://github.com/kreuzwerker/terraform-provider-docker/issues/258))

### Fix

* add current timestamp for file upload to container ([#259](https://github.com/kreuzwerker/terraform-provider-docker/issues/259))


<a name="v2.14.0"></a>
## [v2.14.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.13.0...v2.14.0) (2021-07-09)

### Chore

* prepare release v2.14.0

### Docs

* update to absolute path for registry image context ([#246](https://github.com/kreuzwerker/terraform-provider-docker/issues/246))
* update readme with logos and subsections ([#235](https://github.com/kreuzwerker/terraform-provider-docker/issues/235))

### Feat

* support terraform v1 ([#242](https://github.com/kreuzwerker/terraform-provider-docker/issues/242))

### Fix

* Update the URL of the docker hub registry ([#230](https://github.com/kreuzwerker/terraform-provider-docker/issues/230))


<a name="v2.13.0"></a>
## [v2.13.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.12.2...v2.13.0) (2021-06-22)

### Chore

* prepare release v2.13.0

### Docs

* fix a few typos ([#216](https://github.com/kreuzwerker/terraform-provider-docker/issues/216))
* fix typos in docker_image example usage ([#213](https://github.com/kreuzwerker/terraform-provider-docker/issues/213))


<a name="v2.12.2"></a>
## [v2.12.2](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.12.1...v2.12.2) (2021-05-26)

### Chore

* prepare release v2.12.2


<a name="v2.12.1"></a>
## [v2.12.1](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.12.0...v2.12.1) (2021-05-26)

### Chore

* update changelog for v2.12.1

### Fix

* add service host flattener with space split ([#205](https://github.com/kreuzwerker/terraform-provider-docker/issues/205))
* service state upgradeV2 for empty auth


<a name="v2.12.0"></a>
## [v2.12.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.11.0...v2.12.0) (2021-05-23)

### Chore

* update changelog for v2.12.0
* ignore dist folder
* configure actions/stale ([#157](https://github.com/kreuzwerker/terraform-provider-docker/issues/157))
* add the guide about Terraform Configuration in Bug Report ([#139](https://github.com/kreuzwerker/terraform-provider-docker/issues/139))
* bump docker dependency to v20.10.5 ([#119](https://github.com/kreuzwerker/terraform-provider-docker/issues/119))

### Ci

* run acceptance tests with multiple Terraform versions ([#129](https://github.com/kreuzwerker/terraform-provider-docker/issues/129))

### Docs

* update for v2.12.0
* add releasing steps
* format `Guide of Bug report` ([#159](https://github.com/kreuzwerker/terraform-provider-docker/issues/159))
* add an example to build an image with docker_image ([#158](https://github.com/kreuzwerker/terraform-provider-docker/issues/158))
* add a guide about writing issues to CONTRIBUTING.md ([#149](https://github.com/kreuzwerker/terraform-provider-docker/issues/149))
* fix Github repository URL in README ([#136](https://github.com/kreuzwerker/terraform-provider-docker/issues/136))

### Feat

* support darwin arm builds and golang 1.16 ([#140](https://github.com/kreuzwerker/terraform-provider-docker/issues/140))
* migrate to terraform-sdk v2 ([#102](https://github.com/kreuzwerker/terraform-provider-docker/issues/102))

### Fix

* rewriting tar header fields ([#198](https://github.com/kreuzwerker/terraform-provider-docker/issues/198))
* test spaces for windows ([#190](https://github.com/kreuzwerker/terraform-provider-docker/issues/190))
* replace for loops with StateChangeConf ([#182](https://github.com/kreuzwerker/terraform-provider-docker/issues/182))
* skip sign on compile action
* assign map to rawState when it is nil to prevent panic ([#180](https://github.com/kreuzwerker/terraform-provider-docker/issues/180))
* search local images with Docker image ID ([#151](https://github.com/kreuzwerker/terraform-provider-docker/issues/151))
* set "ForceNew: true" to labelSchema ([#152](https://github.com/kreuzwerker/terraform-provider-docker/issues/152))


<a name="v2.11.0"></a>
## [v2.11.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.10.0...v2.11.0) (2021-01-22)

### Chore

* update changelog for v2.11.0
* updates changelog for v2.10.0

### Docs

* fix legacy configuration style ([#126](https://github.com/kreuzwerker/terraform-provider-docker/issues/126))

### Feat

* add properties -it (tty and stdin_opn) to docker container


<a name="v2.10.0"></a>
## [v2.10.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.9.0...v2.10.0) (2021-01-08)

### Chore

* updates changelog for 2.10.0
* ignores testing folders
* adds separate bug and ft req templates

### Ci

* bumps to docker version 20.10.1
* pins workflows to ubuntu:20.04 image

### Docs

* add labels to arguments of docker_service ([#105](https://github.com/kreuzwerker/terraform-provider-docker/issues/105))
* cleans readme
* adds coc and contributing

### Feat

* supports Docker plugin ([#35](https://github.com/kreuzwerker/terraform-provider-docker/issues/35))
* support max replicas of Docker Service Task Spec ([#112](https://github.com/kreuzwerker/terraform-provider-docker/issues/112))
* add force_remove option to r/image ([#104](https://github.com/kreuzwerker/terraform-provider-docker/issues/104))
* add local semantic commit validation ([#99](https://github.com/kreuzwerker/terraform-provider-docker/issues/99))
* add ability to lint/check of links in documentation locally ([#98](https://github.com/kreuzwerker/terraform-provider-docker/issues/98))

### Fix

* set "latest" to tag when tag isn't specified ([#117](https://github.com/kreuzwerker/terraform-provider-docker/issues/117))
* image label for workflows
* remove all azure cps

### Pull Requests

* Merge pull request [#38](https://github.com/kreuzwerker/terraform-provider-docker/issues/38) from kreuzwerker/ci-ubuntu2004-workflow
* Merge pull request [#36](https://github.com/kreuzwerker/terraform-provider-docker/issues/36) from kreuzwerker/chore-gh-issue-tpl


<a name="v2.9.0"></a>
## [v2.9.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.8.0...v2.9.0) (2020-12-25)

### Chore

* updates changelog for 2.9.0
* update changelog 2.8.0 release date
* introduces golangci-lint ([#32](https://github.com/kreuzwerker/terraform-provider-docker/issues/32))
* fix changelog links

### Ci

* add gofmt's '-s' option
* remove unneeded make tasks
* fix test of website

### Doc

* devices is a block, not a boolean

### Feat

* adds support for OCI manifests ([#316](https://github.com/kreuzwerker/terraform-provider-docker/issues/316))
* adds security_opts to container config. ([#308](https://github.com/kreuzwerker/terraform-provider-docker/issues/308))
* adds support for init process injection for containers. ([#300](https://github.com/kreuzwerker/terraform-provider-docker/issues/300))

### Fix

* changing mounts requires ForceNew ([#314](https://github.com/kreuzwerker/terraform-provider-docker/issues/314))
* allow healthcheck to be computed as container can specify ([#312](https://github.com/kreuzwerker/terraform-provider-docker/issues/312))
* treat null user as a no-op ([#318](https://github.com/kreuzwerker/terraform-provider-docker/issues/318))
* workdir null behavior ([#320](https://github.com/kreuzwerker/terraform-provider-docker/issues/320))

### Style

* format with gofumpt

### Pull Requests

* Merge pull request [#33](https://github.com/kreuzwerker/terraform-provider-docker/issues/33) from brandonros/patch-1
* Merge pull request [#11](https://github.com/kreuzwerker/terraform-provider-docker/issues/11) from suzuki-shunsuke/format-with-gofumpt
* Merge pull request [#26](https://github.com/kreuzwerker/terraform-provider-docker/issues/26) from kreuzwerker/ci/fix-website-ci
* Merge pull request [#8](https://github.com/kreuzwerker/terraform-provider-docker/issues/8) from dubo-dubon-duponey/patch1


<a name="v2.8.0"></a>
## v2.8.0 (2020-11-11)

### Chore

* updates changelog for 2.8.0
* removes travis.yml
* deactivates travis
* removes vendor dir ([#298](https://github.com/kreuzwerker/terraform-provider-docker/issues/298))
* bump go 115 ([#297](https://github.com/kreuzwerker/terraform-provider-docker/issues/297))
* documentation updates ([#286](https://github.com/kreuzwerker/terraform-provider-docker/issues/286))
* updates link syntax ([#287](https://github.com/kreuzwerker/terraform-provider-docker/issues/287))
* fix typo ([#292](https://github.com/kreuzwerker/terraform-provider-docker/issues/292))

### Ci

* reactivats all workflows
* fix website
* only run website workflow
* exports gopath manually
* fix absolute gopath for website
* make website check separate workflow
* fix workflow names
* adds website test to unit test
* adds acc test
* adds compile
* adds go version and goproxy env
* enables unit tests for master branch
* adds unit test workflow
* adds goreleaser and gh action
* bumps docker and ubuntu versions ([#241](https://github.com/kreuzwerker/terraform-provider-docker/issues/241))
* removes debug option from acc tests
* skips test which is flaky only on travis

### Deps

* github.com/hashicorp/terraform[@sdk](https://github.com/sdk)-v0.11-with-go-modules Updated via: go get github.com/hashicorp/terraform[@sdk](https://github.com/sdk)-v0.11-with-go-modules and go mod tidy
* use go modules for dep mgmt run go mod tidy remove govendor from makefile and travis config set appropriate env vars for go modules

### Docker

* improve validation of runtime constraints

### Docs

* update container.html.markdown ([#278](https://github.com/kreuzwerker/terraform-provider-docker/issues/278))
* update service.html.markdown ([#281](https://github.com/kreuzwerker/terraform-provider-docker/issues/281))
* update restart_policy for service. Closes [#228](https://github.com/kreuzwerker/terraform-provider-docker/issues/228)
* adds new label structure. Closes [#214](https://github.com/kreuzwerker/terraform-provider-docker/issues/214)
* update anchors with -1 suffix ([#178](https://github.com/kreuzwerker/terraform-provider-docker/issues/178))
* Fix misspelled words
* Fix exported attribute name in docker_registry_image
* Fix example for docker_registry_image ([#8308](https://github.com/kreuzwerker/terraform-provider-docker/issues/8308))
* provider/docker - network settings attrs

### Feat

* conditionally adding port binding ([#293](https://github.com/kreuzwerker/terraform-provider-docker/issues/293)).
* adds docker Image build feature ([#283](https://github.com/kreuzwerker/terraform-provider-docker/issues/283))
* adds complete support for Docker credential helpers ([#253](https://github.com/kreuzwerker/terraform-provider-docker/issues/253))
* Expose IPv6 properties as attributes
* allow use of source file instead of content / content_base64 ([#240](https://github.com/kreuzwerker/terraform-provider-docker/issues/240))
* supports to update docker_container ([#236](https://github.com/kreuzwerker/terraform-provider-docker/issues/236))
* support to import some docker_container's attributes ([#234](https://github.com/kreuzwerker/terraform-provider-docker/issues/234))
* adds config file content as plain string ([#232](https://github.com/kreuzwerker/terraform-provider-docker/issues/232))
* make UID, GID, & mode for secrets and configs configurable ([#231](https://github.com/kreuzwerker/terraform-provider-docker/issues/231))
* adds import for resources ([#196](https://github.com/kreuzwerker/terraform-provider-docker/issues/196))
* add container ipc mode. ([#182](https://github.com/kreuzwerker/terraform-provider-docker/issues/182))
* adds container working dir ([#181](https://github.com/kreuzwerker/terraform-provider-docker/issues/181))

### Fix

* ignores 'remove_volumes' on container import
* duplicated buildImage function
* port objects with the same internal port but different protocol trigger recreation of container ([#274](https://github.com/kreuzwerker/terraform-provider-docker/issues/274))
* panic to migrate schema of docker_container from v1 to v2 ([#271](https://github.com/kreuzwerker/terraform-provider-docker/issues/271)). Closes [#264](https://github.com/kreuzwerker/terraform-provider-docker/issues/264)
* pins docker registry for tests to v2.7.0
* prevent force recreate of container about some attributes ([#269](https://github.com/kreuzwerker/terraform-provider-docker/issues/269))
* service endpoint spec flattening
* corrects IPAM config read on the data provider ([#229](https://github.com/kreuzwerker/terraform-provider-docker/issues/229))
* replica to 0 in current schema. Closes [#221](https://github.com/kreuzwerker/terraform-provider-docker/issues/221)
* label for network and volume after improt
* binary upload as base 64 content ([#194](https://github.com/kreuzwerker/terraform-provider-docker/issues/194))
* service env truncation for multiple delimiters ([#193](https://github.com/kreuzwerker/terraform-provider-docker/issues/193))
* destroy_grace_seconds are considered ([#179](https://github.com/kreuzwerker/terraform-provider-docker/issues/179))

### Make

* Add website + website-test targets

### Provider

* Ensured Go 1.11 in TravisCI and README provider: Run go fix provider: Run go fmt provider: Encode go version 1.11.5 to .go-version file
* Require Go 1.11 in TravisCI and README provider: Run go fix provider: Run go fmt

### Tests

* Skip test if swap limit isn't available ([#136](https://github.com/kreuzwerker/terraform-provider-docker/issues/136))
* Simplify Dockerfile(s)

### Vendor

* github.com/hashicorp/terraform/...[@v0](https://github.com/v0).10.0
* Ignore github.com/hashicorp/terraform/backend

### Website

* Docs sweep for lists & maps
* note on docker
* docker docs

### Pull Requests

* Merge pull request [#134](https://github.com/kreuzwerker/terraform-provider-docker/issues/134) from terraform-providers/go-modules-2019-03-01
* Merge pull request [#135](https://github.com/kreuzwerker/terraform-provider-docker/issues/135) from terraform-providers/t-simplify-dockerfile
* Merge pull request [#47](https://github.com/kreuzwerker/terraform-provider-docker/issues/47) from captn3m0/docker-link-warning
* Merge pull request [#60](https://github.com/kreuzwerker/terraform-provider-docker/issues/60) from terraform-providers/f-make-website
* Merge pull request [#23](https://github.com/kreuzwerker/terraform-provider-docker/issues/23) from JamesLaverack/patch-1
* Merge pull request [#18](https://github.com/kreuzwerker/terraform-provider-docker/issues/18) from terraform-providers/vendor-tf-0.10
* Merge pull request [#5046](https://github.com/kreuzwerker/terraform-provider-docker/issues/5046) from tpounds/use-built-in-schema-string-hash
* Merge pull request [#3761](https://github.com/kreuzwerker/terraform-provider-docker/issues/3761) from ryane/f-provider-docker-improvements
* Merge pull request [#3383](https://github.com/kreuzwerker/terraform-provider-docker/issues/3383) from apparentlymart/docker-container-command-docs
* Merge pull request [#1564](https://github.com/kreuzwerker/terraform-provider-docker/issues/1564) from nickryand/docker_links




---

# README

**File:** `README.md`
**Tipo:** `.md`
**Dimensione:** 4.3 KB
**Ultima modifica:** 15/06/2026 12:48

---

<a href="https://docker.com">
    <img src="https://raw.githubusercontent.com/kreuzwerker/terraform-provider-docker/master/assets/docker-logo.png" alt="Docker logo" title="Docker" align="right" height="100" />
</a>
<a href="https://terraform.io">
    <img src="https://raw.githubusercontent.com/kreuzwerker/terraform-provider-docker/master/assets/terraform-logo.png" alt="Terraform logo" title="Terraform" align="right" height="100" />
</a>
<a href="https://kreuzwerker.de">
    <img src="https://raw.githubusercontent.com/kreuzwerker/terraform-provider-docker/master/assets/xw-logo.png" alt="Kreuzwerker logo" title="Kreuzwerker" align="right" height="100" />
</a>

# Terraform Provider for Docker

[![Release](https://img.shields.io/github/v/release/kreuzwerker/terraform-provider-docker)](https://github.com/kreuzwerker/terraform-provider-docker/releases)
[![Installs](https://img.shields.io/badge/dynamic/json?logo=terraform&label=installs&query=$.data.attributes.downloads&url=https%3A%2F%2Fregistry.terraform.io%2Fv2%2Fproviders%2F713)](https://registry.terraform.io/providers/kreuzwerker/docker)
[![Registry](https://img.shields.io/badge/registry-doc%40latest-lightgrey?logo=terraform)](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/kreuzwerker/terraform-provider-docker/blob/main/LICENSE)  
[![Go Status](https://github.com/kreuzwerker/terraform-provider-docker/workflows/Acc%20Tests/badge.svg)](https://github.com/kreuzwerker/terraform-provider-docker/actions)
[![Lint Status](https://github.com/kreuzwerker/terraform-provider-docker/workflows/golangci-lint/badge.svg)](https://github.com/kreuzwerker/terraform-provider-docker/actions)
[![Go Report Card](https://goreportcard.com/badge/github.com/kreuzwerker/terraform-provider-docker)](https://goreportcard.com/report/github.com/kreuzwerker/terraform-provider-docker)  

## Documentation

The documentation for the provider is available on the [Terraform Registry](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs).

Do you want to migrate from `v2.x` to `v3.x`? Please read the [migration guide](docs/v2_v3_migration.md)

## Example usage

Take a look at the examples in the [documentation](https://registry.terraform.io/providers/kreuzwerker/docker/3.9.0/docs) of the registry
or use the following example:


```hcl
# Set the required provider and versions
terraform {
  required_providers {
    # We recommend pinning to the specific version of the Docker Provider you're using
    # since new versions are released frequently
    docker = {
      source  = "kreuzwerker/docker"
      version = "3.9.0"
    }
  }
}

# Configure the docker provider
provider "docker" {
}

# Create a docker image resource
# -> docker pull nginx:latest
resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = true
}

# Create a docker container resource
# -> same as 'docker run --name nginx -p8080:80 -d nginx:latest'
resource "docker_container" "nginx" {
  name    = "nginx"
  image   = docker_image.nginx.image_id

  ports {
    external = 8080
    internal = 80
  }
}

# Or create a service resource
# -> same as 'docker service create -d -p 8081:80 --name nginx-service --replicas 2 nginx:latest'
resource "docker_service" "nginx_service" {
  name = "nginx-service"
  task_spec {
    container_spec {
      image = docker_image.nginx.repo_digest
    }
  }

  mode {
    replicated {
      replicas = 2
    }
  }

  endpoint_spec {
    ports {
      published_port = 8081
      target_port    = 80
    }
  }
}
```

## Building The Provider

[Go](https://golang.org/doc/install) 1.18.x (to build the provider plugin)


```sh
$ git clone git@github.com:kreuzwerker/terraform-provider-docker
$ make build
```

## Contributing

The Terraform Docker Provider is the work of many of contributors. We appreciate your help!

To contribute, please read the contribution guidelines: [Contributing to Terraform - Docker Provider](CONTRIBUTING.md)

## License

The Terraform Provider Docker is available to everyone under the terms of the Mozilla Public License Version 2.0. [Take a look the LICENSE file](LICENSE).


## Stargazers over time

[![Stargazers over time](https://starchart.cc/kreuzwerker/terraform-provider-docker.svg)](https://starchart.cc/kreuzwerker/terraform-provider-docker)



---

# main

**File:** `main.py`
**Tipo:** `.py`
**Dimensione:** 0.9 KB
**Ultima modifica:** 15/06/2026 12:46

---

from fastapi import FastAPI
import sqlite3
import os

app = FastAPI()

# Assicura la directory persistente
os.makedirs("/data", exist_ok=True)
DB_PATH = "/data/repository.db"

# Crea il DB e la tabella se non esistono
conn = sqlite3.connect(DB_PATH)
conn.execute("""CREATE TABLE IF NOT EXISTS utenti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)""")
conn.commit()
conn.close()

@app.get("/")
def home():
    return {"msg": "API pronta"}

@app.get("/add/{nome}")
def add(nome: str):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT INTO utenti (nome) VALUES (?)", (nome,))
    conn.commit()
    conn.close()
    return {"msg": f"{nome} aggiunto"}

@app.get("/lista")
def lista():
    conn = sqlite3.connect(DB_PATH)
    utenti = conn.execute("SELECT * FROM utenti").fetchall()
    conn.close()
    return {"utenti": utenti}
#


---

# README

**File:** `README.md`
**Tipo:** `.md`
**Dimensione:** 0.8 KB
**Ultima modifica:** 15/06/2026 12:46

---

Viene allestito un ambiente per arrivare a provare una versione didattica semplificata di IaC, usando OpenTofu e Docker.

## Ambiente
Installare/verificare il SW necessario.  

'OpenTofu'  

Da PowerShell:  
~$ winget install --exact --id=OpenTofu.Tofu  

Chiudere e riaprire PowerShell:  
~$ tofu version  

'Docker' gia installato  

## Esecuzione
Clonare il repository in locale.

Struttura del progetto:  

WSA-lab/  
│  
├─ app/  
│  ├─ main.py  
│  └─ requirements.txt  
│  
├─ Dockerfile  
├─ main.tf  
└─ outputs.tf  

In questa fase si lancia l’app main.py con OpenTofu.  
Spostarsi nella cartella WSA-lab, eseguire i comandi:  
~$ tofu init  
~$ tofu plan  
~$ tofu apply  

Per terminare l'infrastruttura:  
~$ tofu destroy



---

# main

**File:** `main.py`
**Tipo:** `.py`
**Dimensione:** 0.9 KB
**Ultima modifica:** 15/06/2026 11:35

---

from fastapi import FastAPI
import sqlite3
import os

app = FastAPI()

# Assicura la directory persistente
os.makedirs("data", exist_ok=True)
DB_PATH = "data/repository.db"

# Crea il DB e la tabella se non esistono
conn = sqlite3.connect(DB_PATH)
conn.execute("""CREATE TABLE IF NOT EXISTS utenti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)""")
conn.commit()
conn.close()

@app.get("/")
def home():
    return {"msg": "API pronta"}

@app.get("/add/{nome}")
def add(nome: str):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT INTO utenti (nome) VALUES (?)", (nome,))
    conn.commit()
    conn.close()
    return {"msg": f"{nome} aggiunto"}

@app.get("/lista")
def lista():
    conn = sqlite3.connect(DB_PATH)
    utenti = conn.execute("SELECT * FROM utenti").fetchall()
    conn.close()
    return {"utenti": utenti}
#


---

# docker-compose

**File:** `docker-compose.yaml`
**Tipo:** `.yaml`
**Dimensione:** 0.1 KB
**Ultima modifica:** 15/06/2026 11:35

---

services:
  api:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - db_data:/app/data

volumes:
  db_data:


---

# list

**File:** `list.py`
**Tipo:** `.py`
**Dimensione:** 0.1 KB
**Ultima modifica:** 15/06/2026 11:35

---

import os

for e in os.listdir('.'):
    print(e)


---

# README

**File:** `README.md`
**Tipo:** `.md`
**Dimensione:** 4.6 KB
**Ultima modifica:** 15/06/2026 11:35

---

# container-lab

Strumenti utilizzati:
- git
- Docker
 
## Accesso all’ambiente di laboratorio

Verifiche iniziali:

~$ docker --version  
~$ git --version  

Per installare git, da Powershell:  
~$ winget install --id Git.Git -e  

Per installare Docker, da browser:  
https://www.docker.com/products/docker-desktop/  

## Obiettivi
- Capire i comandi base di Docker
- Creare e avviare container manualmente
- Comprendere networking Docker di base

## Esercizio 1

~$ docker run hello-world  

## Preparazione Esercizio 2 ed Esercizio 3

Clonare il repository GitHub corrente su Cloud shell. Attraverso questa operazione saranno scaricate 2 cartelle contenenti i file degli Esercizi 1 e 2.

~$ git clone https://github.com/paolobelloni-its/ITS-Docker.git

## Esercizio 2

~$ spostarsi nella cartella scaricata LISTA

Il programma python (list.py) in questa cartella fa la lista dei file e delle cartelle presenti nella directory corrente.

### Creare immagine

~$ docker build -t immagine-lista .

NOTA: il punto alla fine della riga fa parte del comando!

#### SPIEGAZIONE
docker build: avvia la costruzione di una immagine Docker

-t immagine-lista: assegna un nome (tag) all’immagine costruita

. : indica il contesto di build, cioè la directory corrente (Docker cerca qui il Dockerfile)

Al termine, l’immagine è salvata localmente.
Verificare la presenza dell’immagine con il comando:

~$ docker images

(
nel caso servisse cancellare immagine:

~$ docker rmi nome-immagine

)

Con il comando seguente si possno vedere le caratteristiche dell'immagine:

~$ docker inspect nome-immagine

### Avvio del container

~$ docker run -it immagine-lista

#### SPIEGAZIONE
docker run: crea e avvia un container

-i: mantiene aperto lo standard input

-t: alloca un terminale (TTY)

immagine-lista: nome dell’immagine da usare

Il container viene eseguito in primo piano

Per uscire dal container: exit

### Terminare il container

Per terminare il container:

~$ docker stop <container_id>

Al termine, verificare la lista dei container in esecuzione con il comando:

~$ docker ps  
oppure  
~$ docker ps -a   
per vedere i container sia in esecuzione che terminati.


## Esercizio 3

~$ spostarsi nella cartella scaricata API

Il programma python (list.py) in questa cartella crea un web server (basato su UVICORN) che espone 3 Application Programming Interface sul localhost:
/ - indica che il server e' pronto ed in ascolto
/add/<nome> - inserisce <nome> in un database SQL creato all'interno del container
/lista - mostra i nomi inseriti nel database

A differenza di esercizio 2, il container in esercizio 3 resta in esecuzione finche' non venga terminato.

### Creare immagine

~$ docker build -t immagine-api .

NOTA: il punto alla fine della riga fa parte del comando!

### Avvio del container

~$ docker run -d -p 8000:8000 --name nome-container immagine-api

#### SPIEGAZIONE
-d: lancia il container in background permettendo di usare ancora la command line interface

-p: esponde la porta 8000 interna al container sulla porta 8000 esternamente al container su host (mappa la porta interna al container 8000 sulla porta 8000 dell'host)

--name: assegna un nome al container, di default il nome e' casuale

### Osservare il container

~$ docker inspect nome-container

oppure:

~$ docker stats nome-container

### Gestire le risorse del container in fase di avvio

~$ docker run -m 512m nome-immagine  
limita la RAM del container a 512MB

~$ docker run --cpus=1 nome-immagine  
assegna al container 1 CPU

~$ docker run --cpu-period=100000 --cpu-quota=50000 nome-immagine
assegna al container 1 una quota di 50ms in un periodo di tempo 100ms (equivale ad usare 0.5 CPU)

~$ docker run --pids-limit 50 nome-immagine
limita il numero dei processi in un container a 50

### Terminare il container

Per terminare il container:

~$ docker stop <container_id>  

## Esercizio 4

Voglio utilizzare un programma non installato sulla mia macchina; posso creare un container con un sistema operativo adatto ed installarlo al suo interno.  
Esempio: SQL  

~$ docker run -it --name ubuntu-sql ubuntu bash  
~$~ apt update  
~$~ apt install -y sqlite3  
~$~ sqlite3 test.db  
.exit  
exit  

# Author  

Paolo Belloni  

📧 paolo.belloni@its-ictpiemonte.it

🎓 Course Information  
Institution: ITS Academy ICt Piemonte 
Course: OS e Sistemi di Virtualizzazione  
Language: Labs in Italian  
📄 License  
Educational materials for ITS Academy.  

Last Updated: April 2026  



---

# CHANGELOG

**File:** `CHANGELOG.md`
**Tipo:** `.md`
**Dimensione:** 97.8 KB
**Ultima modifica:** 16/06/2026 11:53

---

# Changelog

<a name="v4.4.0"></a>
## [v4.4.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v4.3.0...v4.4.0) (2026-05-15)



### Feat

* add `docker_system_prune` Plugin Framework action (#928) ([#928](https://github.com/kreuzwerker/terraform-provider-docker/issues/928))

* Add actions for Docker image save/load and container export (#931) ([#931](https://github.com/kreuzwerker/terraform-provider-docker/issues/931))


### Fix

* Align different docker urls to fix authentication issues (#927) ([#927](https://github.com/kreuzwerker/terraform-provider-docker/issues/927))

* canonicalize registry addresses to prevent auth errors (#929) ([#929](https://github.com/kreuzwerker/terraform-provider-docker/issues/929))

* Honor `host_path` in `docker_container.volumes` when both source fields are set (#930) ([#930](https://github.com/kreuzwerker/terraform-provider-docker/issues/930))

* Use configured host instead of daemon host for dockercli client (#939) ([#939](https://github.com/kreuzwerker/terraform-provider-docker/issues/939))


<a name="v4.3.0"></a>
## [v4.3.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v4.2.0...v4.3.0) (2026-05-10)



### Chore

* update dependency golangci/golangci-lint to v2.12.2 (#919) ([#919](https://github.com/kreuzwerker/terraform-provider-docker/issues/919))

* Update README and improve renovate (#923) ([#923](https://github.com/kreuzwerker/terraform-provider-docker/issues/923))

* pin dependencies (#924) ([#924](https://github.com/kreuzwerker/terraform-provider-docker/issues/924))

* migrate config renovate.json5 (#925) ([#925](https://github.com/kreuzwerker/terraform-provider-docker/issues/925))

* Prepare release v4.3.0 (#926) ([#926](https://github.com/kreuzwerker/terraform-provider-docker/issues/926))


### Feat

* expose provenance and sbom schema fields for buildx builds (#840) ([#840](https://github.com/kreuzwerker/terraform-provider-docker/issues/840) [#826](https://github.com/kreuzwerker/terraform-provider-docker/issues/826))

* Add docker_compose resource (#918) ([#918](https://github.com/kreuzwerker/terraform-provider-docker/issues/918))

* Add plaintext `data_raw` input for human-readable `docker_config` diffs (#913) ([#913](https://github.com/kreuzwerker/terraform-provider-docker/issues/913))


### Fix

* update module github.com/docker/go-connections to v0.7.0 (#908) ([#908](https://github.com/kreuzwerker/terraform-provider-docker/issues/908))

* update module github.com/hashicorp/terraform-plugin-docs to v0.25.0 (#911) ([#911](https://github.com/kreuzwerker/terraform-provider-docker/issues/911))

* update module github.com/hashicorp/terraform-plugin-testing to v1.16.0 (#912) ([#912](https://github.com/kreuzwerker/terraform-provider-docker/issues/912))

* update module github.com/hashicorp/terraform-plugin-sdk/v2 to v2.40.1 (#914) ([#914](https://github.com/kreuzwerker/terraform-provider-docker/issues/914))

* update module github.com/masterminds/semver/v3 to v3.5.0 (#916) ([#916](https://github.com/kreuzwerker/terraform-provider-docker/issues/916))


<a name="v4.2.0"></a>
## [v4.2.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v4.1.0...v4.2.0) (2026-04-14)



### Chore

* Replace git-chglog with git-cliff (#904) ([#904](https://github.com/kreuzwerker/terraform-provider-docker/issues/904))

* Prepare release 4.2.0 (#907) ([#907](https://github.com/kreuzwerker/terraform-provider-docker/issues/907))


### Docs

* add missing docker_exec/buildx examples and align action name to docker_exec (#898) ([#898](https://github.com/kreuzwerker/terraform-provider-docker/issues/898))


### Feat

* Expose attached container network addresses in `docker_network` data source (#897) ([#897](https://github.com/kreuzwerker/terraform-provider-docker/issues/897))

* Add docker import action (#900) ([#900](https://github.com/kreuzwerker/terraform-provider-docker/issues/900))

* Implement docker registry image tags data source (#903) ([#903](https://github.com/kreuzwerker/terraform-provider-docker/issues/903))


### Fix

* Fix `docker_container.container_logs` to return demultiplexed log content (#899) ([#899](https://github.com/kreuzwerker/terraform-provider-docker/issues/899))

* Normalize `docker_service` `max_failure_ratio` diffs to prevent `0` vs `0.0` drift (#901) ([#901](https://github.com/kreuzwerker/terraform-provider-docker/issues/901))

* Fix flaky `docker_container` destroy by disabling link removal during delete (#902) ([#902](https://github.com/kreuzwerker/terraform-provider-docker/issues/902))

* update module github.com/hashicorp/terraform-plugin-mux to v0.23.1 (#905) ([#905](https://github.com/kreuzwerker/terraform-provider-docker/issues/905))

* update module github.com/masterminds/semver/v3 to v3.4.0 (#906) ([#906](https://github.com/kreuzwerker/terraform-provider-docker/issues/906))


<a name="v4.1.0"></a>
## [v4.1.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v4.0.0...v4.1.0) (2026-04-09)



### Chore

* Prepare release 4.1.0 (#896) ([#896](https://github.com/kreuzwerker/terraform-provider-docker/issues/896))


### Feat

* Implement docker_exec action (#885) ([#885](https://github.com/kreuzwerker/terraform-provider-docker/issues/885))

* Allow `docker_registry_image.auth_config` to mirror provider `registry_auth` optional credentials (#887) ([#887](https://github.com/kreuzwerker/terraform-provider-docker/issues/887))

* Add `platform` support to `docker_container` for cross-architecture emulation (#886) ([#886](https://github.com/kreuzwerker/terraform-provider-docker/issues/886))

* Add Plugin Framework `docker_containers` data source for Docker container enumeration (#893) ([#893](https://github.com/kreuzwerker/terraform-provider-docker/issues/893))


### Fix

* update module github.com/containerd/platforms to v1.0.0-rc.4 (#889) ([#889](https://github.com/kreuzwerker/terraform-provider-docker/issues/889))

* Make container deletion idempotent for missing containers (#891) ([#891](https://github.com/kreuzwerker/terraform-provider-docker/issues/891) [#890](https://github.com/kreuzwerker/terraform-provider-docker/issues/890))

* Fix `docker_service` platform flattening hash to prevent platform list drift on updates (#892) ([#892](https://github.com/kreuzwerker/terraform-provider-docker/issues/892))


### Other

* Avoid `docker_container` replacement when only daemon default `log_opts` are present (#888) ([#888](https://github.com/kreuzwerker/terraform-provider-docker/issues/888))

* Prevent `docker_container` read panic with CDI `device_requests` by hardening device flattening (#895) ([#895](https://github.com/kreuzwerker/terraform-provider-docker/issues/895))


<a name="v4.0.0"></a>
## [v4.0.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.9.0...v4.0.0) (2026-04-03)



### Chore

* Add deprecation for docker_service.networks_advanced.name (#837) ([#837](https://github.com/kreuzwerker/terraform-provider-docker/issues/837))

* update actions/checkout action to v6 (#825) ([#825](https://github.com/kreuzwerker/terraform-provider-docker/issues/825))

* update hashicorp/setup-terraform action to v4 (#860) ([#860](https://github.com/kreuzwerker/terraform-provider-docker/issues/860))

* update docker/setup-docker-action action to v5 (#866) ([#866](https://github.com/kreuzwerker/terraform-provider-docker/issues/866))

* update dependency golangci/golangci-lint to v2.10.1 (#869) ([#869](https://github.com/kreuzwerker/terraform-provider-docker/issues/869))

* update dependency golangci/golangci-lint to v2.11.4 (#871) ([#871](https://github.com/kreuzwerker/terraform-provider-docker/issues/871))

* Prepare 4.0.0 release (#884) ([#884](https://github.com/kreuzwerker/terraform-provider-docker/issues/884))


### Feat

* Add muxing to introduce new plugin framework (#838) ([#838](https://github.com/kreuzwerker/terraform-provider-docker/issues/838))

* Multiple enhancements (#854) ([#854](https://github.com/kreuzwerker/terraform-provider-docker/issues/854) [#543](https://github.com/kreuzwerker/terraform-provider-docker/issues/543) [#777](https://github.com/kreuzwerker/terraform-provider-docker/issues/777) [#588](https://github.com/kreuzwerker/terraform-provider-docker/issues/588))

* Make buildx builder default (#855) ([#855](https://github.com/kreuzwerker/terraform-provider-docker/issues/855))

* Add new docker container attributes (#857) ([#857](https://github.com/kreuzwerker/terraform-provider-docker/issues/857))

* Add CDI device support (#762) ([#762](https://github.com/kreuzwerker/terraform-provider-docker/issues/762))

* Implement proper parsing of GPU device requests when using gpus… (#881) ([#881](https://github.com/kreuzwerker/terraform-provider-docker/issues/881))

* add selinux_relabel attribute to docker_container volumes (#883) ([#883](https://github.com/kreuzwerker/terraform-provider-docker/issues/883))


### Fix

* update module golang.org/x/sync to v0.19.0 (#828) ([#828](https://github.com/kreuzwerker/terraform-provider-docker/issues/828))

* update module github.com/hashicorp/terraform-plugin-log to v0.10.0 (#823) ([#823](https://github.com/kreuzwerker/terraform-provider-docker/issues/823))

* update module github.com/morikuni/aec to v1.1.0 (#829) ([#829](https://github.com/kreuzwerker/terraform-provider-docker/issues/829))

* update module google.golang.org/protobuf to v1.36.11 (#830) ([#830](https://github.com/kreuzwerker/terraform-provider-docker/issues/830))

* update module github.com/sirupsen/logrus to v1.9.4 (#836) ([#836](https://github.com/kreuzwerker/terraform-provider-docker/issues/836))

* Refactor docker container state handling to properly restart when exited (#841) ([#841](https://github.com/kreuzwerker/terraform-provider-docker/issues/841))

* docker container stopped ports (#842) ([#842](https://github.com/kreuzwerker/terraform-provider-docker/issues/842))

* correctly set docker_container devices (#843) ([#843](https://github.com/kreuzwerker/terraform-provider-docker/issues/843))

* update module github.com/katbyte/terrafmt to v0.5.6 (#844) ([#844](https://github.com/kreuzwerker/terraform-provider-docker/issues/844))

* update module github.com/hashicorp/terraform-plugin-sdk/v2 to v2.38.2 (#847) ([#847](https://github.com/kreuzwerker/terraform-provider-docker/issues/847))

* Use DOCKER_CONFIG env same way as with docker cli (#849) ([#849](https://github.com/kreuzwerker/terraform-provider-docker/issues/849))

* calculation of Dockerfile path in docker_image build (#853) ([#853](https://github.com/kreuzwerker/terraform-provider-docker/issues/853))

* update module github.com/hashicorp/terraform-plugin-go to v0.30.0 (#861) ([#861](https://github.com/kreuzwerker/terraform-provider-docker/issues/861))

* update module github.com/hashicorp/terraform-plugin-framework to v1.18.0 (#862) ([#862](https://github.com/kreuzwerker/terraform-provider-docker/issues/862))

* update module github.com/hashicorp/terraform-plugin-mux to v0.22.0 (#863) ([#863](https://github.com/kreuzwerker/terraform-provider-docker/issues/863))

* update module github.com/hashicorp/terraform-plugin-sdk/v2 to v2.39.0 (#864) ([#864](https://github.com/kreuzwerker/terraform-provider-docker/issues/864))

* update module golang.org/x/sync to v0.20.0 (#872) ([#872](https://github.com/kreuzwerker/terraform-provider-docker/issues/872))

* Handle size_bytes in tmpfs_options in docker_service (#882) ([#882](https://github.com/kreuzwerker/terraform-provider-docker/issues/882))

* tests for healthcheck is not required for docker container resource (#834) ([#834](https://github.com/kreuzwerker/terraform-provider-docker/issues/834))


### Other

* Prevent `docker_registry_image` panic on registries returning nil body without digest header (#880) ([#880](https://github.com/kreuzwerker/terraform-provider-docker/issues/880))


<a name="v3.9.0"></a>
## [v3.9.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.8.0...v3.9.0) (2025-11-09)



### Chore

* Prepare release v3.8.0 (#806) ([#806](https://github.com/kreuzwerker/terraform-provider-docker/issues/806))

* Add file requested by hashicorp (#813) ([#813](https://github.com/kreuzwerker/terraform-provider-docker/issues/813))

* update golangci/golangci-lint-action action to v9 (#819) ([#819](https://github.com/kreuzwerker/terraform-provider-docker/issues/819))

* Prepare release v3.9.0 (#821) ([#821](https://github.com/kreuzwerker/terraform-provider-docker/issues/821))


### Feat

* Implement caching of docker provider (#808) ([#808](https://github.com/kreuzwerker/terraform-provider-docker/issues/808))


### Fix

* update module github.com/hashicorp/terraform-plugin-docs to v0.24.0 (#807) ([#807](https://github.com/kreuzwerker/terraform-provider-docker/issues/807))

* docker_service label can be updated without recreate (#814) ([#814](https://github.com/kreuzwerker/terraform-provider-docker/issues/814))

* test attribute of docker_service healthcheck is not required (#815) ([#815](https://github.com/kreuzwerker/terraform-provider-docker/issues/815))

* update module github.com/docker/cli to v28.5.2+incompatible (#816) ([#816](https://github.com/kreuzwerker/terraform-provider-docker/issues/816))

* update module github.com/docker/docker to v28.5.2+incompatible (#817) ([#817](https://github.com/kreuzwerker/terraform-provider-docker/issues/817))

* update module golang.org/x/sync to v0.18.0 (#820) ([#820](https://github.com/kreuzwerker/terraform-provider-docker/issues/820))


<a name="v3.8.0"></a>
## [v3.8.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.7.0...v3.8.0) (2025-10-08)



### Feat

* Implement docker cluster volume (#793) ([#793](https://github.com/kreuzwerker/terraform-provider-docker/issues/793))

* implement mac_address for networks_advanced (#794) ([#794](https://github.com/kreuzwerker/terraform-provider-docker/issues/794))

* Add build option for additional contexts (#798) ([#798](https://github.com/kreuzwerker/terraform-provider-docker/issues/798))

* Add build attribute for docker_registry_image (#805) ([#805](https://github.com/kreuzwerker/terraform-provider-docker/issues/805))


### Fix

* update module google.golang.org/protobuf to v1.36.8 (#775) ([#775](https://github.com/kreuzwerker/terraform-provider-docker/issues/775))

* update module google.golang.org/protobuf to v1.36.9 (#787) ([#787](https://github.com/kreuzwerker/terraform-provider-docker/issues/787))

* omit sending systempaths=unconfied to daemon (#796) ([#796](https://github.com/kreuzwerker/terraform-provider-docker/issues/796))

* Recreate builder if deleted out-of-band (#797) ([#797](https://github.com/kreuzwerker/terraform-provider-docker/issues/797))

* update module golang.org/x/sync to v0.17.0 (#785) ([#785](https://github.com/kreuzwerker/terraform-provider-docker/issues/785))

* update module github.com/hashicorp/terraform-plugin-docs to v0.23.0 (#788) ([#788](https://github.com/kreuzwerker/terraform-provider-docker/issues/788))

* update module github.com/hashicorp/terraform-plugin-sdk/v2 to v2.38.1 (#789) ([#789](https://github.com/kreuzwerker/terraform-provider-docker/issues/789))

* update module github.com/docker/cli to v28.4.0+incompatible (#781) ([#781](https://github.com/kreuzwerker/terraform-provider-docker/issues/781))

* update module google.golang.org/protobuf to v1.36.10 (#799) ([#799](https://github.com/kreuzwerker/terraform-provider-docker/issues/799))

* update module github.com/docker/cli to v28.5.0+incompatible (#800) ([#800](https://github.com/kreuzwerker/terraform-provider-docker/issues/800))

* update module github.com/docker/docker to v28.5.0+incompatible (#782) ([#782](https://github.com/kreuzwerker/terraform-provider-docker/issues/782))

* update module github.com/docker/docker to v28.5.1+incompatible (#804) ([#804](https://github.com/kreuzwerker/terraform-provider-docker/issues/804))

* update module github.com/docker/cli to v28.5.1+incompatible (#803) ([#803](https://github.com/kreuzwerker/terraform-provider-docker/issues/803))


<a name="v3.7.0"></a>
## [v3.7.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.6.2...v3.7.0) (2025-08-19)



### Chore

* update dependency go to v1.24.5 (#757) ([#757](https://github.com/kreuzwerker/terraform-provider-docker/issues/757))

* update dependency go to v1.24.6 (#764) ([#764](https://github.com/kreuzwerker/terraform-provider-docker/issues/764))

* update actions/checkout action to v5 (#768) ([#768](https://github.com/kreuzwerker/terraform-provider-docker/issues/768))

* Prepare release v3.7.0 (#774) ([#774](https://github.com/kreuzwerker/terraform-provider-docker/issues/774))


### Feat

* Add timeout support to docker_registry_image resource (#769) ([#769](https://github.com/kreuzwerker/terraform-provider-docker/issues/769))

* Implement cache_from and cache_to for docker_image (#772) ([#772](https://github.com/kreuzwerker/terraform-provider-docker/issues/772))

* Implement memory_reservation and network_mode enhancements (#773) ([#773](https://github.com/kreuzwerker/terraform-provider-docker/issues/773))


### Fix

* update module github.com/hashicorp/terraform-plugin-docs to v0.22.0 (#755) ([#755](https://github.com/kreuzwerker/terraform-provider-docker/issues/755))

* update module golang.org/x/sync to v0.16.0 (#758) ([#758](https://github.com/kreuzwerker/terraform-provider-docker/issues/758))

* update module google.golang.org/protobuf to v1.36.7 (#765) ([#765](https://github.com/kreuzwerker/terraform-provider-docker/issues/765))

* update module github.com/docker/go-connections to v0.6.0 (#766) ([#766](https://github.com/kreuzwerker/terraform-provider-docker/issues/766))

* Correctly get and set nanoCPUs for docker_container (#771) ([#771](https://github.com/kreuzwerker/terraform-provider-docker/issues/771))


<a name="v3.6.2"></a>
## [v3.6.2](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.6.1...v3.6.2) (2025-06-13)



### Chore

* Prepare release v3.6.2 (#750) ([#750](https://github.com/kreuzwerker/terraform-provider-docker/issues/750))


### Feat

* Allow digest in image name (#744) ([#744](https://github.com/kreuzwerker/terraform-provider-docker/issues/744))


### Fix

* Typo in cgroup_parent handling (#746) ([#746](https://github.com/kreuzwerker/terraform-provider-docker/issues/746) [#745](https://github.com/kreuzwerker/terraform-provider-docker/issues/745))

* Reading non existant volume should recreate (#749) ([#749](https://github.com/kreuzwerker/terraform-provider-docker/issues/749))

* Remove wrong buildkit version assignment (#747) ([#747](https://github.com/kreuzwerker/terraform-provider-docker/issues/747))


<a name="v3.6.1"></a>
## [v3.6.1](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.6.0...v3.6.1) (2025-06-05)



### Chore

* Add retryon429 for markdownlint (#736) ([#736](https://github.com/kreuzwerker/terraform-provider-docker/issues/736))

* update dependency go to v1.24.4 (#742) ([#742](https://github.com/kreuzwerker/terraform-provider-docker/issues/742))

* Prepare release v3.6.1 (#743) ([#743](https://github.com/kreuzwerker/terraform-provider-docker/issues/743))


### Feat

* allow to set the cgroup parent for container (#609) ([#609](https://github.com/kreuzwerker/terraform-provider-docker/issues/609))


### Fix

* update module golang.org/x/sync to v0.15.0 (#741) ([#741](https://github.com/kreuzwerker/terraform-provider-docker/issues/741))


<a name="v3.6.0"></a>
## [v3.6.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.5.0...v3.6.0) (2025-05-25)



### Chore

* update dependency go to v1.24.3 (#719) ([#719](https://github.com/kreuzwerker/terraform-provider-docker/issues/719))

* update golangci/golangci-lint-action action to v8 (#718) ([#718](https://github.com/kreuzwerker/terraform-provider-docker/issues/718))

* Prepare release v3.6.0 (#735) ([#735](https://github.com/kreuzwerker/terraform-provider-docker/issues/735))


### Feat

* implement Buildx builder resource (#724) ([#724](https://github.com/kreuzwerker/terraform-provider-docker/issues/724))

* Add implementaion of capabilities in docker servic (#727) ([#727](https://github.com/kreuzwerker/terraform-provider-docker/issues/727))

* Implement correct cpu scheduler settings (#732) ([#732](https://github.com/kreuzwerker/terraform-provider-docker/issues/732))


### Fix

* update module google.golang.org/protobuf to v1.36.6 (#720) ([#720](https://github.com/kreuzwerker/terraform-provider-docker/issues/720))

* update module github.com/hashicorp/terraform-plugin-sdk/v2 to v2.37.0 (#726) ([#726](https://github.com/kreuzwerker/terraform-provider-docker/issues/726))

* update module github.com/containerd/console to v1.0.5 (#729) ([#729](https://github.com/kreuzwerker/terraform-provider-docker/issues/729))

* Make endpoint validation less strict (#733) ([#733](https://github.com/kreuzwerker/terraform-provider-docker/issues/733))

* update module github.com/moby/buildkit to v0.22.0 (#731) ([#731](https://github.com/kreuzwerker/terraform-provider-docker/issues/731))

* Implement buildx fixes for general buildkit support and platform handling (#734) ([#734](https://github.com/kreuzwerker/terraform-provider-docker/issues/734))


<a name="v3.5.0"></a>
## [v3.5.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.4.0...v3.5.0) (2025-05-06)



### Chore

* Prepare release v3.5.0 (#721) ([#721](https://github.com/kreuzwerker/terraform-provider-docker/issues/721))


### Feat

* Implement healthcheck start interval (#713) ([#713](https://github.com/kreuzwerker/terraform-provider-docker/issues/713))

* Implement registry_image_manifests data source (#714) ([#714](https://github.com/kreuzwerker/terraform-provider-docker/issues/714))

* Support registries that return empty auth scope #646 ([#646](https://github.com/kreuzwerker/terraform-provider-docker/issues/646))

* Implement using of buildx for docker_image (#717) ([#717](https://github.com/kreuzwerker/terraform-provider-docker/issues/717))


<a name="v3.4.0"></a>
## [v3.4.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.3.0...v3.4.0) (2025-04-25)



### Chore

* Prepare release v3.4.0 (#712) ([#712](https://github.com/kreuzwerker/terraform-provider-docker/issues/712))


### Feat

* Implement volume_options subpath (#710) ([#710](https://github.com/kreuzwerker/terraform-provider-docker/issues/710))


### Fix

* Use auth_config block also for registry_image delete functionality (#708) ([#708](https://github.com/kreuzwerker/terraform-provider-docker/issues/708))

* Improve container wait handling (#709) ([#709](https://github.com/kreuzwerker/terraform-provider-docker/issues/709))

* Prevent recreation of image name is intentionally set to a fixed value (#711) ([#711](https://github.com/kreuzwerker/terraform-provider-docker/issues/711))


<a name="v3.3.0"></a>
## [v3.3.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.2.0...v3.3.0) (2025-04-19)



### Chore

* Update docker/docker and docker/cli to newest stable (#695) ([#695](https://github.com/kreuzwerker/terraform-provider-docker/issues/695))

* Update terraform-plugin-sdk/v2 dependency (#699) ([#699](https://github.com/kreuzwerker/terraform-provider-docker/issues/699))

* update dependency go to v1.24.2 (#700) ([#700](https://github.com/kreuzwerker/terraform-provider-docker/issues/700))

* Prepare release v3.3.0 (#705) ([#705](https://github.com/kreuzwerker/terraform-provider-docker/issues/705))


### Feat

* Implement auth_config for docker_registry_image (#701) ([#701](https://github.com/kreuzwerker/terraform-provider-docker/issues/701))

* Implement tag triggers for docker_tag resource (#702) ([#702](https://github.com/kreuzwerker/terraform-provider-docker/issues/702))

* disable_docker_daemon_check for provider (#703) ([#703](https://github.com/kreuzwerker/terraform-provider-docker/issues/703))

* Implement support for docker context (#704) ([#704](https://github.com/kreuzwerker/terraform-provider-docker/issues/704))


### Fix

* Store correctly ports from server (#698) ([#698](https://github.com/kreuzwerker/terraform-provider-docker/issues/698))


<a name="v3.2.0"></a>
## [v3.2.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.1.2...v3.2.0) (2025-04-16)



### Chore

* Upgrade golangci-lint to next major version (#686) ([#686](https://github.com/kreuzwerker/terraform-provider-docker/issues/686))

* Prepare release v3.2.0 (#694) ([#694](https://github.com/kreuzwerker/terraform-provider-docker/issues/694))


### Docs

* Consolidated update of docs from several PRs (#691) ([#691](https://github.com/kreuzwerker/terraform-provider-docker/issues/691))


### Feat

* Add support for build-secrets (#604) ([#604](https://github.com/kreuzwerker/terraform-provider-docker/issues/604))

* Implement docker_image timeouts (#692) ([#692](https://github.com/kreuzwerker/terraform-provider-docker/issues/692))

* Implement upload permissions in docker_container resource (#693) ([#693](https://github.com/kreuzwerker/terraform-provider-docker/issues/693))


### Fix

* Authentication to ECR public (#690) ([#690](https://github.com/kreuzwerker/terraform-provider-docker/issues/690))


<a name="v3.1.2"></a>
## [v3.1.2](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.1.1...v3.1.2) (2025-04-15)



### Other

* prepare release 3.1.2 (#688) ([#688](https://github.com/kreuzwerker/terraform-provider-docker/issues/688))


<a name="v3.1.1"></a>
## [v3.1.1](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.1.0...v3.1.1) (2025-04-14)



### Other

* Prepare release 3.1.1 (#687) ([#687](https://github.com/kreuzwerker/terraform-provider-docker/issues/687))


<a name="v3.1.0"></a>
## [v3.1.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.0.2...v3.1.0) (2025-04-14)



### Chore

* update Go version to 1.22 for consistency across workflows, jo… (#613) ([#613](https://github.com/kreuzwerker/terraform-provider-docker/issues/613))

* update golangci/golangci-lint-action action to v6 (#615) ([#615](https://github.com/kreuzwerker/terraform-provider-docker/issues/615))

* update hashicorp/setup-terraform action to v3 (#616) ([#616](https://github.com/kreuzwerker/terraform-provider-docker/issues/616))

* Prepare release 3.1.0 (#685) ([#685](https://github.com/kreuzwerker/terraform-provider-docker/issues/685))


### Feat

* support setting cpu shares (#575) ([#575](https://github.com/kreuzwerker/terraform-provider-docker/issues/575))


### Fix

* update module github.com/katbyte/terrafmt to v0.5.3 (#614) ([#614](https://github.com/kreuzwerker/terraform-provider-docker/issues/614))

* update module github.com/golangci/golangci-lint to v1.59.0 (#474) ([#474](https://github.com/kreuzwerker/terraform-provider-docker/issues/474))

* Set correct default network driver and fix a test (#677) ([#677](https://github.com/kreuzwerker/terraform-provider-docker/issues/677))

* Compress build context before sending it to Docker (#461) ([#461](https://github.com/kreuzwerker/terraform-provider-docker/issues/461) [#439](https://github.com/kreuzwerker/terraform-provider-docker/issues/439))

* update module github.com/katbyte/terrafmt to v0.5.4 (#654) ([#654](https://github.com/kreuzwerker/terraform-provider-docker/issues/654))

* update module github.com/docker/cli to v20.10.27+incompatible (#675) ([#675](https://github.com/kreuzwerker/terraform-provider-docker/issues/675))

* update module github.com/hashicorp/go-cty to v1.5.0 (#679) ([#679](https://github.com/kreuzwerker/terraform-provider-docker/issues/679))

* update module github.com/docker/go-connections to v0.5.0 (#673) ([#673](https://github.com/kreuzwerker/terraform-provider-docker/issues/673))

* Use build_args everywhere and update documentation (#681) ([#681](https://github.com/kreuzwerker/terraform-provider-docker/issues/681))

* update module github.com/docker/docker to v20.10.27+incompatible (#509) ([#509](https://github.com/kreuzwerker/terraform-provider-docker/issues/509))


### Other

* s/presend/present/ (#606) ([#606](https://github.com/kreuzwerker/terraform-provider-docker/issues/606))

* update-dockerignore-for-context-ignore (#625) ([#625](https://github.com/kreuzwerker/terraform-provider-docker/issues/625))

* ✨ Update Terraform version to 1.8.x in acceptance test GitHub Actions workflow. (#626) ([#626](https://github.com/kreuzwerker/terraform-provider-docker/issues/626))

* Ignore error message case in comparison for ignorable messages. (#583) ([#583](https://github.com/kreuzwerker/terraform-provider-docker/issues/583))


<a name="v3.0.2"></a>
## [v3.0.2](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.0.1...v3.0.2) (2023-03-17)



### Chore

* Prepare release v3.0.2


### Docs

* correct spelling of "networks_advanced" (#517) ([#517](https://github.com/kreuzwerker/terraform-provider-docker/issues/517))


### Feat

* add MAC address to state (#523) ([#523](https://github.com/kreuzwerker/terraform-provider-docker/issues/523))


### Fix

* update module github.com/hashicorp/terraform-plugin-sdk/v2 to v2.25.0 (#515) ([#515](https://github.com/kreuzwerker/terraform-provider-docker/issues/515))

* update module github.com/hashicorp/terraform-plugin-docs to v0.14.1 (#519) ([#519](https://github.com/kreuzwerker/terraform-provider-docker/issues/519))

* Implement proxy support. (#529) ([#529](https://github.com/kreuzwerker/terraform-provider-docker/issues/529))


<a name="v3.0.1"></a>
## [v3.0.1](https://github.com/kreuzwerker/terraform-provider-docker/compare/v3.0.0...v3.0.1) (2023-01-13)



### Chore

* Prepare release v3.0.1


### Fix

* Access health of container correctly. (#506) ([#506](https://github.com/kreuzwerker/terraform-provider-docker/issues/506))


<a name="v3.0.0"></a>
## [v3.0.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.25.0...v3.0.0) (2023-01-13)



### Chore

* Prepare release v3.0.0


### Docs

* Add migration guide and update README (#502) ([#502](https://github.com/kreuzwerker/terraform-provider-docker/issues/502))

* Update documentation.


### Feat

* Prepare v3 release (#503) ([#503](https://github.com/kreuzwerker/terraform-provider-docker/issues/503))


<a name="v2.25.0"></a>
## [v2.25.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.24.0...v2.25.0) (2023-01-05)



### Chore

* Prepare release v2.25.0


### Docs

* Add documentation of remote hosts. (#498) ([#498](https://github.com/kreuzwerker/terraform-provider-docker/issues/498))


### Feat

* Add sysctl implementation to container of docker_service. (#499) ([#499](https://github.com/kreuzwerker/terraform-provider-docker/issues/499))

* Add platform attribute to docker_image resource (#500) ([#500](https://github.com/kreuzwerker/terraform-provider-docker/issues/500))

* add alias for networks (#241) ([#241](https://github.com/kreuzwerker/terraform-provider-docker/issues/241))

* Migrate build block to `docker_image` (#501) ([#501](https://github.com/kreuzwerker/terraform-provider-docker/issues/501))


<a name="v2.24.0"></a>
## [v2.24.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.23.1...v2.24.0) (2022-12-23)



### Chore

* update goreleaser/goreleaser-action action to v4 (#485) ([#485](https://github.com/kreuzwerker/terraform-provider-docker/issues/485))

* Prepare release v2.24.0


### Docs

* Update command typo (#487) ([#487](https://github.com/kreuzwerker/terraform-provider-docker/issues/487))

* Fix generated website.


### Feat

* add IPAM options block for docker networks (#491) ([#491](https://github.com/kreuzwerker/terraform-provider-docker/issues/491))

* Support registries with disabled auth (#494) ([#494](https://github.com/kreuzwerker/terraform-provider-docker/issues/494))

* Add triggers attribute to docker_registry_image (#496) ([#496](https://github.com/kreuzwerker/terraform-provider-docker/issues/496))

* cgroupns support (#497) ([#497](https://github.com/kreuzwerker/terraform-provider-docker/issues/497))


### Fix

* Pin data source specific tag test to older tag.

* update module github.com/docker/cli to v20.10.22+incompatible (#489) ([#489](https://github.com/kreuzwerker/terraform-provider-docker/issues/489))

* update module github.com/docker/docker to v20.10.22+incompatible (#490) ([#490](https://github.com/kreuzwerker/terraform-provider-docker/issues/490))


### Test

* Add test for parsing auth headers.


<a name="v2.23.1"></a>
## [v2.23.1](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.23.0...v2.23.1) (2022-11-23)



### Chore

* Prepare release v2.23.1


### Fix

* Set OS_ARCH from GOHOSTOS and GOHOSTARCH (#477) ([#477](https://github.com/kreuzwerker/terraform-provider-docker/issues/477))

* update module github.com/moby/buildkit to v0.10.6 (#478) ([#478](https://github.com/kreuzwerker/terraform-provider-docker/issues/478))

* update module github.com/hashicorp/terraform-plugin-sdk/v2 to v2.24.1 (#479) ([#479](https://github.com/kreuzwerker/terraform-provider-docker/issues/479))

* Handle Auth Header Scopes (#482) ([#482](https://github.com/kreuzwerker/terraform-provider-docker/issues/482))

* Update shasum of busybox:1.35.0 tag in test.


<a name="v2.23.0"></a>
## [v2.23.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.22.0...v2.23.0) (2022-11-02)



### Chore

* Prepare release v2.23.0


### Feat

* add docker logs data source (#471) ([#471](https://github.com/kreuzwerker/terraform-provider-docker/issues/471))

* wait container healthy state (#467) ([#467](https://github.com/kreuzwerker/terraform-provider-docker/issues/467))


### Fix

* Correct provider name to match the public registry (#462) ([#462](https://github.com/kreuzwerker/terraform-provider-docker/issues/462))

* Update shasum of busybox:1.35.0 tag

* update module github.com/golangci/golangci-lint to v1.50.0 (#469) ([#469](https://github.com/kreuzwerker/terraform-provider-docker/issues/469))

* update module github.com/moby/buildkit to v0.10.5 (#472) ([#472](https://github.com/kreuzwerker/terraform-provider-docker/issues/472))

* update module github.com/hashicorp/terraform-plugin-sdk/v2 to v2.24.0 (#456) ([#456](https://github.com/kreuzwerker/terraform-provider-docker/issues/456))

* Update shasum of busybox:1.35.0 tag in test.

* update module github.com/docker/cli to v20.10.21+incompatible (#457) ([#457](https://github.com/kreuzwerker/terraform-provider-docker/issues/457))

* update module github.com/docker/docker to v20.10.21+incompatible (#459) ([#459](https://github.com/kreuzwerker/terraform-provider-docker/issues/459))


<a name="v2.22.0"></a>
## [v2.22.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.21.0...v2.22.0) (2022-09-20)



### Chore

* Prepare release v2.22.0


### Feat

* Configurable timeout for docker_container resource stateChangeConf (#454) ([#454](https://github.com/kreuzwerker/terraform-provider-docker/issues/454))


### Fix

* oauth authorization support for azurecr (#451) ([#451](https://github.com/kreuzwerker/terraform-provider-docker/issues/451))


<a name="v2.21.0"></a>
## [v2.21.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.20.3...v2.21.0) (2022-09-05)



### Chore

* Prepare release v2.21.0


### Docs

* Fix docker config example.


### Feat

* Update used goversion to 1.18. (#449) ([#449](https://github.com/kreuzwerker/terraform-provider-docker/issues/449))

* Add image_id attribute to docker_image resource. (#450) ([#450](https://github.com/kreuzwerker/terraform-provider-docker/issues/450))


### Fix

* update module github.com/docker/go-units to v0.5.0 (#445) ([#445](https://github.com/kreuzwerker/terraform-provider-docker/issues/445))

* update module github.com/golangci/golangci-lint to v1.49.0 (#441) ([#441](https://github.com/kreuzwerker/terraform-provider-docker/issues/441))

* update module github.com/hashicorp/terraform-plugin-sdk/v2 to v2.21.0 (#434) ([#434](https://github.com/kreuzwerker/terraform-provider-docker/issues/434))

* Fix repo_digest value for DockerImageDatasource test.

* Remove reading part of docker_tag resource. (#448) ([#448](https://github.com/kreuzwerker/terraform-provider-docker/issues/448))

* Replace deprecated .latest attribute with new image_id. (#453) ([#453](https://github.com/kreuzwerker/terraform-provider-docker/issues/453))


<a name="v2.20.3"></a>
## [v2.20.3](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.20.2...v2.20.3) (2022-08-31)



### Chore

* Prepare release v2.20.3


### Fix

* Adding Support for Windows Paths in Bash (#438) ([#438](https://github.com/kreuzwerker/terraform-provider-docker/issues/438))

* update module github.com/katbyte/terrafmt to v0.5.2 (#437) ([#437](https://github.com/kreuzwerker/terraform-provider-docker/issues/437))

* Docker Registry Image data source use HEAD request to query image digest (#433) ([#433](https://github.com/kreuzwerker/terraform-provider-docker/issues/433))

* update module github.com/moby/buildkit to v0.10.4 (#440) ([#440](https://github.com/kreuzwerker/terraform-provider-docker/issues/440))


<a name="v2.20.2"></a>
## [v2.20.2](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.20.1...v2.20.2) (2022-08-10)



### Chore

* Prepare release v2.20.2


### Fix

* Check the operating system for determining the default Docker socket (#427) ([#427](https://github.com/kreuzwerker/terraform-provider-docker/issues/427))

* update module github.com/golangci/golangci-lint to v1.48.0 (#423) ([#423](https://github.com/kreuzwerker/terraform-provider-docker/issues/423) [#431](https://github.com/kreuzwerker/terraform-provider-docker/issues/431))


### Other

* Revert "fix(deps): update module github.com/golangci/golangci-lint to v1.48.0 (#423)" ([#423](https://github.com/kreuzwerker/terraform-provider-docker/issues/423))


<a name="v2.20.1"></a>
## [v2.20.1](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.20.0...v2.20.1) (2022-08-10)



### Chore

* Reduce time to setup AccTests (#430) ([#430](https://github.com/kreuzwerker/terraform-provider-docker/issues/430))

* Prepare release v2.20.1


### Docs

* Improve docker network usage documentation [skip-ci]


### Feat

* Implement triggers attribute for docker_image. (#425) ([#425](https://github.com/kreuzwerker/terraform-provider-docker/issues/425))


### Fix

* update module github.com/hashicorp/terraform-plugin-sdk/v2 to v2.20.0 (#422) ([#422](https://github.com/kreuzwerker/terraform-provider-docker/issues/422))

* update module github.com/golangci/golangci-lint to v1.47.2 (#411) ([#411](https://github.com/kreuzwerker/terraform-provider-docker/issues/411))

* Add ForceTrue to docker_image name attribute. (#421) ([#421](https://github.com/kreuzwerker/terraform-provider-docker/issues/421))

* update module github.com/katbyte/terrafmt to v0.5.1 (#429) ([#429](https://github.com/kreuzwerker/terraform-provider-docker/issues/429))


<a name="v2.20.0"></a>
## [v2.20.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.19.0...v2.20.0) (2022-07-28)



### Chore

* update actions/setup-go action to v3 (#353) ([#353](https://github.com/kreuzwerker/terraform-provider-docker/issues/353))

* update goreleaser/goreleaser-action action to v3 (#389) ([#389](https://github.com/kreuzwerker/terraform-provider-docker/issues/389))

* Fix release targets in Makefile.

* update module go to 1.18 (#412) ([#412](https://github.com/kreuzwerker/terraform-provider-docker/issues/412))

* Prepare release v2.20.0


### Feat

* Implement support for insecure registries (#414) ([#414](https://github.com/kreuzwerker/terraform-provider-docker/issues/414))

* Implementation of `docker_tag` resource. (#418) ([#418](https://github.com/kreuzwerker/terraform-provider-docker/issues/418))


### Fix

* update module github.com/hashicorp/terraform-plugin-sdk/v2 to v2.19.0 (#410) ([#410](https://github.com/kreuzwerker/terraform-provider-docker/issues/410))


<a name="v2.19.0"></a>
## [v2.19.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.18.1...v2.19.0) (2022-07-15)



### Chore

* Prepare release v2.19.0


### Feat

* Add gpu flag to docker_container resource (#405) ([#405](https://github.com/kreuzwerker/terraform-provider-docker/issues/405))


### Fix

* ECR authentication (#409) ([#409](https://github.com/kreuzwerker/terraform-provider-docker/issues/409))

* Enable authentication to multiple registries again. (#400) ([#400](https://github.com/kreuzwerker/terraform-provider-docker/issues/400))


<a name="v2.18.1"></a>
## [v2.18.1](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.18.0...v2.18.1) (2022-07-14)



### Chore

* update actions/checkout action to v3 (#354) ([#354](https://github.com/kreuzwerker/terraform-provider-docker/issues/354))

* Automate changelog generation [skip ci]

* Prepare release v2.18.1


### Fix

* Enables having a Dockerfile outside the context (#402) ([#402](https://github.com/kreuzwerker/terraform-provider-docker/issues/402))

* Throw errors when any part of docker config file handling goes wrong. (#406) ([#406](https://github.com/kreuzwerker/terraform-provider-docker/issues/406))

* Improve searchLocalImages error handling. (#407) ([#407](https://github.com/kreuzwerker/terraform-provider-docker/issues/407))

* update module github.com/moby/buildkit to v0.10.3 (#394) ([#394](https://github.com/kreuzwerker/terraform-provider-docker/issues/394))


<a name="v2.18.0"></a>
## [v2.18.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.17.0...v2.18.0) (2022-07-11)



### Chore

* prepare release v2.18.0


### Feat

* add runtime, stop_signal and stop_timeout properties to the docker_container resource (#364) ([#364](https://github.com/kreuzwerker/terraform-provider-docker/issues/364))


### Fix

* update module github.com/docker/distribution to v2.8.1 (#348) ([#348](https://github.com/kreuzwerker/terraform-provider-docker/issues/348))

* update module github.com/golangci/golangci-lint to v1.46.2 (#341) ([#341](https://github.com/kreuzwerker/terraform-provider-docker/issues/341))

* update module github.com/hashicorp/terraform-plugin-sdk/v2 to v2.18.0 (#396) ([#396](https://github.com/kreuzwerker/terraform-provider-docker/issues/396))

* compare relative paths when excluding, fixes kreuzwerker#280 (#397) ([#280](https://github.com/kreuzwerker/terraform-provider-docker/issues/280) [#397](https://github.com/kreuzwerker/terraform-provider-docker/issues/397))

* Switch to proper go tools mechanism to fix website-* workflows. (#399) ([#399](https://github.com/kreuzwerker/terraform-provider-docker/issues/399))

* Correctly handle build files and context for docker_registry_image (#398) ([#398](https://github.com/kreuzwerker/terraform-provider-docker/issues/398))


<a name="v2.17.0"></a>
## [v2.17.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.16.0...v2.17.0) (2022-06-23)



### Chore

* remove the workflow to close stale issues and pull requests (#371) ([#371](https://github.com/kreuzwerker/terraform-provider-docker/issues/371))

* update golangci/golangci-lint-action action to v3 (#352) ([#352](https://github.com/kreuzwerker/terraform-provider-docker/issues/352))

* split acc test into resources (#382) ([#382](https://github.com/kreuzwerker/terraform-provider-docker/issues/382))

* improve image delete error message (#359) ([#359](https://github.com/kreuzwerker/terraform-provider-docker/issues/359))

* Update website-generation workflow (#386) ([#386](https://github.com/kreuzwerker/terraform-provider-docker/issues/386))

* Exclude examples directory from renovate.

* prepare release v2.17.0


### Feat

* Enable buildkit when client has support. (#387) ([#387](https://github.com/kreuzwerker/terraform-provider-docker/issues/387))


### Fix

* correct authentication for ghcr.io registry(#349) ([#349](https://github.com/kreuzwerker/terraform-provider-docker/issues/349))

* update module github.com/docker/cli to v20.10.17 (#324) ([#324](https://github.com/kreuzwerker/terraform-provider-docker/issues/324))

* update module github.com/hashicorp/terraform-plugin-sdk/v2 to v2.17.0 (#357) ([#357](https://github.com/kreuzwerker/terraform-provider-docker/issues/357))

* Pipeline updates (#390) ([#390](https://github.com/kreuzwerker/terraform-provider-docker/issues/390))

* update go package files directly on master to fix build.


<a name="v2.16.0"></a>
## [v2.16.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.15.0...v2.16.0) (2022-01-24)



### Chore

* update alpine docker tag to v3.14.2 (#277) ([#277](https://github.com/kreuzwerker/terraform-provider-docker/issues/277))

* update tj-actions/verify-changed-files action to v7.2 (#285) ([#285](https://github.com/kreuzwerker/terraform-provider-docker/issues/285))

* update nginx:1.21.1 docker digest to a05b0cd (#273) ([#273](https://github.com/kreuzwerker/terraform-provider-docker/issues/273))

* update golang to v1.17 (#272) ([#272](https://github.com/kreuzwerker/terraform-provider-docker/issues/272))

* unify require sections in go.mod files

* update workflows and docs to go 1.17

* update nginx docker tag to v1.21.3 (#287) ([#287](https://github.com/kreuzwerker/terraform-provider-docker/issues/287))

* update nginx:1.21.3 docker digest to 644a705 (#295) ([#295](https://github.com/kreuzwerker/terraform-provider-docker/issues/295))

* update tj-actions/verify-changed-files action to v8 (#299) ([#299](https://github.com/kreuzwerker/terraform-provider-docker/issues/299))

* update tj-actions/verify-changed-files action to v8.3 (#303) ([#303](https://github.com/kreuzwerker/terraform-provider-docker/issues/303))

* update nginx docker tag to v1.21.4 (#309) ([#309](https://github.com/kreuzwerker/terraform-provider-docker/issues/309))

* update tj-actions/verify-changed-files action to v8.8 (#308) ([#308](https://github.com/kreuzwerker/terraform-provider-docker/issues/308))

* prepare release v2.16.0


### Docs

* fix r/registry_image truncated docs (#304) ([#304](https://github.com/kreuzwerker/terraform-provider-docker/issues/304))

* update registry_image.md (#321) ([#321](https://github.com/kreuzwerker/terraform-provider-docker/issues/321))

* fix service options (#337) ([#337](https://github.com/kreuzwerker/terraform-provider-docker/issues/337) [#335](https://github.com/kreuzwerker/terraform-provider-docker/issues/335))


### Feat

* add parameter for SSH options (#335) ([#335](https://github.com/kreuzwerker/terraform-provider-docker/issues/335))


### Fix

* update module github.com/golangci/golangci-lint to v1.42.0 (#274) ([#274](https://github.com/kreuzwerker/terraform-provider-docker/issues/274))

* update module github.com/golangci/golangci-lint to v1.42.1 (#284) ([#284](https://github.com/kreuzwerker/terraform-provider-docker/issues/284))

* update module github.com/hashicorp/terraform-plugin-sdk/v2 to v2.7.1 (#279) ([#279](https://github.com/kreuzwerker/terraform-provider-docker/issues/279))

* fmt of go files for go 1.17

* update module github.com/hashicorp/terraform-plugin-docs to v0.5.0 (#286) ([#286](https://github.com/kreuzwerker/terraform-provider-docker/issues/286))

* update module github.com/hashicorp/terraform-plugin-sdk/v2 to v2.8.0 (#298) ([#298](https://github.com/kreuzwerker/terraform-provider-docker/issues/298))

* update module github.com/docker/cli to v20.10.10 (#296) ([#296](https://github.com/kreuzwerker/terraform-provider-docker/issues/296))

* Fixed typo (#310) ([#310](https://github.com/kreuzwerker/terraform-provider-docker/issues/310))

* remove log_driver's default value and make log_driver `computed` (#270) ([#270](https://github.com/kreuzwerker/terraform-provider-docker/issues/270))

* add nil check of DriverConfig (#315) ([#315](https://github.com/kreuzwerker/terraform-provider-docker/issues/315))

* update module github.com/docker/docker to v20.10.10 (#297) ([#297](https://github.com/kreuzwerker/terraform-provider-docker/issues/297))

* update module github.com/docker/cli to v20.10.11 (#316) ([#316](https://github.com/kreuzwerker/terraform-provider-docker/issues/316))

* update module github.com/hashicorp/terraform-plugin-sdk/v2 to v2.9.0 (#317) ([#317](https://github.com/kreuzwerker/terraform-provider-docker/issues/317))

* update module github.com/hashicorp/terraform-plugin-docs to v0.5.1 (#311) ([#311](https://github.com/kreuzwerker/terraform-provider-docker/issues/311))

* update module github.com/golangci/golangci-lint to v1.43.0 (#306) ([#306](https://github.com/kreuzwerker/terraform-provider-docker/issues/306))

* pass container rm flag (#322) ([#322](https://github.com/kreuzwerker/terraform-provider-docker/issues/322) [#321](https://github.com/kreuzwerker/terraform-provider-docker/issues/321))

* update module github.com/hashicorp/terraform-plugin-sdk/v2 to v2.10.1 (#323) ([#323](https://github.com/kreuzwerker/terraform-provider-docker/issues/323))


<a name="v2.15.0"></a>
## [v2.15.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.14.0...v2.15.0) (2021-08-11)



### Chore

* update nginx:1.21.1 docker digest to 353c20f (#248) ([#248](https://github.com/kreuzwerker/terraform-provider-docker/issues/248))

* update actions/stale action to v4 (#250) ([#250](https://github.com/kreuzwerker/terraform-provider-docker/issues/250))

* update nginx:1.21.1 docker digest to 11d4e59 (#251) ([#251](https://github.com/kreuzwerker/terraform-provider-docker/issues/251))

* update nginx:1.21.1 docker digest to 8f33576 (#252) ([#252](https://github.com/kreuzwerker/terraform-provider-docker/issues/252))

* update alpine docker tag to v3.14.1 (#263) ([#263](https://github.com/kreuzwerker/terraform-provider-docker/issues/263))

* adapt acc test docker version (#266) ([#266](https://github.com/kreuzwerker/terraform-provider-docker/issues/266))

* re go gets terraform-plugin-docs

* prepare release v2.15.0


### Docs

* add badges

* corrects authentication misspell. Closes #264 ([#264](https://github.com/kreuzwerker/terraform-provider-docker/issues/264))


### Feat

* add container storage opts (#258) ([#258](https://github.com/kreuzwerker/terraform-provider-docker/issues/258))


### Fix

* update module github.com/docker/cli to v20.10.8 (#255) ([#255](https://github.com/kreuzwerker/terraform-provider-docker/issues/255))

* update module github.com/docker/docker to v20.10.8 (#256) ([#256](https://github.com/kreuzwerker/terraform-provider-docker/issues/256))

* add current timestamp for file upload to container (#259) ([#259](https://github.com/kreuzwerker/terraform-provider-docker/issues/259))


<a name="v2.14.0"></a>
## [v2.14.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.13.0...v2.14.0) (2021-07-09)



### Chore

* update nginx:1.21.0 docker digest to d1b8ff2 (#232) ([#232](https://github.com/kreuzwerker/terraform-provider-docker/issues/232))

* update tj-actions/verify-changed-files action to v7 (#237) ([#237](https://github.com/kreuzwerker/terraform-provider-docker/issues/237))

* update nginx docker tag to v1.21.1 (#243) ([#243](https://github.com/kreuzwerker/terraform-provider-docker/issues/243))

* prepare release v2.14.0


### Docs

* update readme with logos and subsections (#235) ([#235](https://github.com/kreuzwerker/terraform-provider-docker/issues/235))

* docs/service entrypoint (#244) ([#244](https://github.com/kreuzwerker/terraform-provider-docker/issues/244))

* update to absolute path for registry image context (#246) ([#246](https://github.com/kreuzwerker/terraform-provider-docker/issues/246))


### Feat

* support terraform v1 (#242) ([#242](https://github.com/kreuzwerker/terraform-provider-docker/issues/242))


### Fix

* update module github.com/hashicorp/terraform-plugin-sdk/v2 to v2.7.0 (#236) ([#236](https://github.com/kreuzwerker/terraform-provider-docker/issues/236))

* fix/service bind options (#234) ([#234](https://github.com/kreuzwerker/terraform-provider-docker/issues/234))

* Update the URL of the docker hub registry (#230) ([#230](https://github.com/kreuzwerker/terraform-provider-docker/issues/230))

* consider .dockerignore in image build (#240) ([#240](https://github.com/kreuzwerker/terraform-provider-docker/issues/240))


<a name="v2.13.0"></a>
## [v2.13.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.12.2...v2.13.0) (2021-06-22)



### Chore

* chore/refactor tests (#201) ([#201](https://github.com/kreuzwerker/terraform-provider-docker/issues/201))

* update alpine docker tag to v3.13.5

* update nginx:1.18.0-alpine docker digest to 93baf2e

* update nginx:1.18.0-alpine docker digest to 93baf2e

* update nginx docker tag to v1.21.0

* update nginx docker tag to v1.21.0

* update stocard/gotthard docker digest to 38c2216

* update stocard/gotthard docker digest to 38c2216

* update alpine docker tag to v3.14.0 (#225) ([#225](https://github.com/kreuzwerker/terraform-provider-docker/issues/225))

* prepare release v2.13.0


### Docs

* fix typos in docker_image example usage (#213) ([#213](https://github.com/kreuzwerker/terraform-provider-docker/issues/213))

* fix a few typos (#216) ([#216](https://github.com/kreuzwerker/terraform-provider-docker/issues/216))

* add oneline cli git cmd to get the changes since the last tag


### Fix

* update module github.com/golangci/golangci-lint to v1.40.1 (#194) ([#194](https://github.com/kreuzwerker/terraform-provider-docker/issues/194))

* update module github.com/docker/cli to v20.10.7 (#217) ([#217](https://github.com/kreuzwerker/terraform-provider-docker/issues/217))

* fix/service image name (#212) ([#212](https://github.com/kreuzwerker/terraform-provider-docker/issues/212))

* update module github.com/golangci/golangci-lint to v1.41.1 (#226) ([#226](https://github.com/kreuzwerker/terraform-provider-docker/issues/226))

* update module github.com/docker/docker to v20.10.7 (#218) ([#218](https://github.com/kreuzwerker/terraform-provider-docker/issues/218))

* fix/service delete deadline (#227) ([#227](https://github.com/kreuzwerker/terraform-provider-docker/issues/227))


### Other

* include image name in error message (#223) ([#223](https://github.com/kreuzwerker/terraform-provider-docker/issues/223))


<a name="v2.12.2"></a>
## [v2.12.2](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.12.1...v2.12.2) (2021-05-26)



### Chore

* prepare release v2.12.2


<a name="v2.12.1"></a>
## [v2.12.1](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.12.0...v2.12.1) (2021-05-26)



### Chore

* update tj-actions/verify-changed-files action to v6.2 (#200) ([#200](https://github.com/kreuzwerker/terraform-provider-docker/issues/200))

* update changelog for v2.12.1


### Fix

* service state upgradeV2 for empty auth ([#203](https://github.com/kreuzwerker/terraform-provider-docker/issues/203))

* add service host flattener with space split (#205) ([#205](https://github.com/kreuzwerker/terraform-provider-docker/issues/205))


<a name="v2.12.0"></a>
## [v2.12.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.11.0...v2.12.0) (2021-05-23)



### Chore

* bump docker dependency to v20.10.5 (#119) ([#119](https://github.com/kreuzwerker/terraform-provider-docker/issues/119))

* add the guide about Terraform Configuration in Bug Report (#139) ([#139](https://github.com/kreuzwerker/terraform-provider-docker/issues/139))

* configure actions/stale (#157) ([#157](https://github.com/kreuzwerker/terraform-provider-docker/issues/157))

* configure Renovate (#162) ([#162](https://github.com/kreuzwerker/terraform-provider-docker/issues/162))

* ignore dist folder

* update changelog for v2.12.0


### Ci

* run acceptance tests with multiple Terraform versions (#129) ([#129](https://github.com/kreuzwerker/terraform-provider-docker/issues/129))


### Docs

* fix Github repository URL in README (#136) ([#136](https://github.com/kreuzwerker/terraform-provider-docker/issues/136))

* add a guide about writing issues to CONTRIBUTING.md (#149) ([#149](https://github.com/kreuzwerker/terraform-provider-docker/issues/149))

* update example usage

* add an example to build an image with docker_image (#158) ([#158](https://github.com/kreuzwerker/terraform-provider-docker/issues/158))

* format `Guide of Bug report` (#159) ([#159](https://github.com/kreuzwerker/terraform-provider-docker/issues/159))

* add releasing steps

* update for v2.12.0


### Feat

* migrate to terraform-sdk v2 (#102) ([#102](https://github.com/kreuzwerker/terraform-provider-docker/issues/102))

* support darwin arm builds and golang 1.16 (#140) ([#140](https://github.com/kreuzwerker/terraform-provider-docker/issues/140))

* feat/doc generation (#193) ([#193](https://github.com/kreuzwerker/terraform-provider-docker/issues/193))


### Fix

* set "ForceNew: true" to labelSchema (#152) ([#152](https://github.com/kreuzwerker/terraform-provider-docker/issues/152))

* search local images with Docker image ID (#151) ([#151](https://github.com/kreuzwerker/terraform-provider-docker/issues/151))

* fix/workflows (#169) ([#169](https://github.com/kreuzwerker/terraform-provider-docker/issues/169))

* update module github.com/golangci/golangci-lint to v1.39.0 (#166) ([#166](https://github.com/kreuzwerker/terraform-provider-docker/issues/166))

* update module github.com/katbyte/terrafmt to v0.3.0 (#168) ([#168](https://github.com/kreuzwerker/terraform-provider-docker/issues/168))

* update module github.com/hashicorp/terraform-plugin-sdk/v2 to v2.5.0 (#167) ([#167](https://github.com/kreuzwerker/terraform-provider-docker/issues/167))

* update module github.com/docker/docker to v20.10.5 (#165) ([#165](https://github.com/kreuzwerker/terraform-provider-docker/issues/165))

* update module github.com/docker/cli to v20.10.5 (#164) ([#164](https://github.com/kreuzwerker/terraform-provider-docker/issues/164))

* update module github.com/docker/docker to v20.10.6 (#174) ([#174](https://github.com/kreuzwerker/terraform-provider-docker/issues/174))

* update module github.com/docker/cli to v20.10.6 (#175) ([#175](https://github.com/kreuzwerker/terraform-provider-docker/issues/175))

* fix/move helpers (#170) ([#170](https://github.com/kreuzwerker/terraform-provider-docker/issues/170))

* assign map to rawState when it is nil to prevent panic (#180) ([#180](https://github.com/kreuzwerker/terraform-provider-docker/issues/180))

* remove gpg key from action to make it work in forks

* skip sign on compile action

* update module github.com/hashicorp/terraform-plugin-sdk/v2 to v2.6.1 (#181) ([#181](https://github.com/kreuzwerker/terraform-provider-docker/issues/181))

* replace for loops with StateChangeConf (#182) ([#182](https://github.com/kreuzwerker/terraform-provider-docker/issues/182))

* update module github.com/golangci/golangci-lint to v1.40.0 (#191) ([#191](https://github.com/kreuzwerker/terraform-provider-docker/issues/191))

* test spaces for windows (#190) ([#190](https://github.com/kreuzwerker/terraform-provider-docker/issues/190))

* rewriting tar header fields (#198) ([#198](https://github.com/kreuzwerker/terraform-provider-docker/issues/198) [#192](https://github.com/kreuzwerker/terraform-provider-docker/issues/192))


### Other

* Merge branch 'master' of github.com:kreuzwerker/terraform-provider-docker


<a name="v2.11.0"></a>
## [v2.11.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.9.0...v2.11.0) (2021-01-22)



### Chore

* updates changelog for v2.10.0

* update changelog for v2.11.0


### Ci

* pins workflows to ubuntu:20.04 image

* bumps to docker version 20.10.1


### Docs

* updates links to provider and slack

* fixes broken links

* fixes more broken links

* fixes copy paster

* add labels to arguments of docker_service (#105) ([#105](https://github.com/kreuzwerker/terraform-provider-docker/issues/105) [#103](https://github.com/kreuzwerker/terraform-provider-docker/issues/103))

* fix legacy configuration style (#126) ([#126](https://github.com/kreuzwerker/terraform-provider-docker/issues/126))


### Feat

* add ability to lint/check of links in documentation locally (#98) ([#98](https://github.com/kreuzwerker/terraform-provider-docker/issues/98))

* add local semantic commit validation (#99) ([#99](https://github.com/kreuzwerker/terraform-provider-docker/issues/99))

* add force_remove option to r/image (#104) ([#104](https://github.com/kreuzwerker/terraform-provider-docker/issues/104))

* support max replicas of Docker Service Task Spec (#112) ([#112](https://github.com/kreuzwerker/terraform-provider-docker/issues/112) [#111](https://github.com/kreuzwerker/terraform-provider-docker/issues/111))

* supports Docker plugin (#35) ([#35](https://github.com/kreuzwerker/terraform-provider-docker/issues/35) [#24](https://github.com/kreuzwerker/terraform-provider-docker/issues/24))

* add properties -it (tty and stdin_opn) to docker container ([#120](https://github.com/kreuzwerker/terraform-provider-docker/issues/120))


### Fix

* image label for workflows

* adds issues path in links

* set "latest" to tag when tag isn't specified (#117) ([#117](https://github.com/kreuzwerker/terraform-provider-docker/issues/117))


### Other

* Merge branch 'master' into chore-gh-issue-tpl

* Merge pull request #36 from kreuzwerker/chore-gh-issue-tpl ([#36](https://github.com/kreuzwerker/terraform-provider-docker/issues/36))

* Merge pull request #38 from kreuzwerker/ci-ubuntu2004-workflow ([#38](https://github.com/kreuzwerker/terraform-provider-docker/issues/38))

* aligns braces


<a name="v2.9.0"></a>
## [v2.9.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/v2.8.0...v2.9.0) (2020-12-25)



### Chore

* fix changelog links

* introduces golangci-lint (#32) ([#32](https://github.com/kreuzwerker/terraform-provider-docker/issues/32) [#13](https://github.com/kreuzwerker/terraform-provider-docker/issues/13))

* update changelog 2.8.0 release date

* adds separate bug and ft req templates

* ignores testing folders

* updates changelog for 2.9.0


### Ci

* fix test of website

* remove unneeded make tasks

* add gofmt's '-s' option


### Docs

* devices is a block, not a boolean

* adds coc and contributing

* cleans readme


### Feat

* adds support for init process injection for containers. (#300) ([#300](https://github.com/kreuzwerker/terraform-provider-docker/issues/300))

* adds security_opts to container config. (#308) ([#308](https://github.com/kreuzwerker/terraform-provider-docker/issues/308) [#288](https://github.com/kreuzwerker/terraform-provider-docker/issues/288))

* adds support for OCI manifests (#316) ([#316](https://github.com/kreuzwerker/terraform-provider-docker/issues/316) [#315](https://github.com/kreuzwerker/terraform-provider-docker/issues/315))


### Fix

* workdir null behavior (#320) ([#320](https://github.com/kreuzwerker/terraform-provider-docker/issues/320) [#319](https://github.com/kreuzwerker/terraform-provider-docker/issues/319))

* treat null user as a no-op (#318) ([#318](https://github.com/kreuzwerker/terraform-provider-docker/issues/318) [#317](https://github.com/kreuzwerker/terraform-provider-docker/issues/317))

* allow healthcheck to be computed as container can specify (#312) ([#312](https://github.com/kreuzwerker/terraform-provider-docker/issues/312))

* changing mounts requires ForceNew (#314) ([#314](https://github.com/kreuzwerker/terraform-provider-docker/issues/314))

* Fix crash

* remove all azure cps


### Other

* Merge branch 'master' of github.com:terraform-providers/terraform-provider-docker

* Merge branch 'master' of github.com:terraform-providers/terraform-provider-docker

* Merge branch 'master' of github.com:terraform-providers/terraform-provider-docker

* Merge branch 'master' of github.com:terraform-providers/terraform-provider-docker

* Merge pull request #8 from dubo-dubon-duponey/patch1 ([#8](https://github.com/kreuzwerker/terraform-provider-docker/issues/8))

* Merge pull request #26 from kreuzwerker/ci/fix-website-ci ([#26](https://github.com/kreuzwerker/terraform-provider-docker/issues/26))

* format with gofumpt

* Merge pull request #11 from suzuki-shunsuke/format-with-gofumpt ([#11](https://github.com/kreuzwerker/terraform-provider-docker/issues/11))

* Merge pull request #33 from brandonros/patch-1 ([#33](https://github.com/kreuzwerker/terraform-provider-docker/issues/33))


<a name="v2.8.0"></a>
## [v2.8.0](https://github.com/kreuzwerker/terraform-provider-docker/compare/...v2.8.0) (2020-11-11)



### Chore

* adapts cp debug outputs

* fix typo (#292) ([#292](https://github.com/kreuzwerker/terraform-provider-docker/issues/292))

* updates link syntax (#287) ([#287](https://github.com/kreuzwerker/terraform-provider-docker/issues/287))

* documentation updates (#286) ([#286](https://github.com/kreuzwerker/terraform-provider-docker/issues/286))

* bump go 115 (#297) ([#297](https://github.com/kreuzwerker/terraform-provider-docker/issues/297))

* removes vendor dir (#298) ([#298](https://github.com/kreuzwerker/terraform-provider-docker/issues/298))

* deactivates travis

* removes travis.yml

* updates changelog for 2.8.0


### Ci

* skips test which is flaky only on travis

* removes debug option from acc tests

* bumps docker and ubuntu versions (#241) ([#241](https://github.com/kreuzwerker/terraform-provider-docker/issues/241))

* adds goreleaser and gh action

* adds unit test workflow

* enables unit tests for master branch

* adds go version and goproxy env

* adds compile

* adds acc test

* adds website test to unit test

* fix workflow names

* make website check separate workflow

* fix gopath

* switches from free to openbsd

* fix absolute gopath for website

* exports gopath manually

* consolidates all cmds into 1

* only run website workflow

* fix website

* reactivats all workflows


### Docs

* improve validation of runtime constraints

* provider/docker - network settings attrs

* Document new data source + limitations (#7814) ([#7814](https://github.com/kreuzwerker/terraform-provider-docker/issues/7814))

* Fix example for docker_registry_image (#8308) ([#8308](https://github.com/kreuzwerker/terraform-provider-docker/issues/8308))

* Fix exported attribute name in docker_registry_image

* Fix misspelled words

* docker_container resource mounts support (#147) ([#147](https://github.com/kreuzwerker/terraform-provider-docker/issues/147))

* docker_network data source (#87). Closes #84 ([#87](https://github.com/kreuzwerker/terraform-provider-docker/issues/87) [#84](https://github.com/kreuzwerker/terraform-provider-docker/issues/84))

* update anchors with -1 suffix (#178) ([#178](https://github.com/kreuzwerker/terraform-provider-docker/issues/178) [#176](https://github.com/kreuzwerker/terraform-provider-docker/issues/176))

* adds new label structure. Closes #214 ([#214](https://github.com/kreuzwerker/terraform-provider-docker/issues/214))

* update restart_policy for service. Closes #228 ([#228](https://github.com/kreuzwerker/terraform-provider-docker/issues/228))

* update service.html.markdown (#281) ([#281](https://github.com/kreuzwerker/terraform-provider-docker/issues/281))

* update container.html.markdown (#278) ([#278](https://github.com/kreuzwerker/terraform-provider-docker/issues/278))


### Feat

* Add Issue Template

* Added Docker links support to the docker_container resource.

* Add docker container network settings to output attribute

* Added support for more complexly images repos such as images on a private registry that are stored as namespace/name

* Add privileged option to docker container resource

* Add network_mode support to docker

* Add support of custom networks in docker

* Add the networks entry

* Add Elem and Set to the network set

* Add `destroy_grace_seconds` option to stop container before delete (#7513) ([#7513](https://github.com/kreuzwerker/terraform-provider-docker/issues/7513))

* Allow Windows Docker containers to map volumes (#13584) ([#13584](https://github.com/kreuzwerker/terraform-provider-docker/issues/13584))

* Added Docker links support to the docker_container resource.

* Add privileged option to docker container resource

* Add network_mode support to docker

* Add support of custom networks in docker

* Add the networks entry

* Add `destroy_grace_seconds` option to stop container before delete (#7513) ([#7513](https://github.com/kreuzwerker/terraform-provider-docker/issues/7513))

* Adding back the GNUmakefile test-compile step

* Feat/private registry support (#21) ([#21](https://github.com/kreuzwerker/terraform-provider-docker/issues/21))

* Allow the awslogs log driver (#28) ([#28](https://github.com/kreuzwerker/terraform-provider-docker/issues/28))

* Feat/swarm 1 update deps (#37) ([#37](https://github.com/kreuzwerker/terraform-provider-docker/issues/37))

* Feat/swarm 2 refactorings (#38) ([#38](https://github.com/kreuzwerker/terraform-provider-docker/issues/38))

* Feat/swarm 3 acc test infra (#39) ([#39](https://github.com/kreuzwerker/terraform-provider-docker/issues/39))

* Add support to attach devices to containers (#54) ([#54](https://github.com/kreuzwerker/terraform-provider-docker/issues/54))

* Add ability to upload executable files (#55) ([#55](https://github.com/kreuzwerker/terraform-provider-docker/issues/55))

* Add Ulimits to containers (#35) ([#35](https://github.com/kreuzwerker/terraform-provider-docker/issues/35))

* Feat/swarm 4 new resources (#40) ([#40](https://github.com/kreuzwerker/terraform-provider-docker/issues/40))

* Adds warning about the link feature

* Add support for running tests on Windows (#90) ([#90](https://github.com/kreuzwerker/terraform-provider-docker/issues/90))

* Adds pid and namespace mode (#96) ([#96](https://github.com/kreuzwerker/terraform-provider-docker/issues/96) [#88](https://github.com/kreuzwerker/terraform-provider-docker/issues/88) [#17](https://github.com/kreuzwerker/terraform-provider-docker/issues/17))

* Add labels to support docker stacks (#92) ([#92](https://github.com/kreuzwerker/terraform-provider-docker/issues/92))

* Add rm and attach options to execute short-lived containers (#106) ([#106](https://github.com/kreuzwerker/terraform-provider-docker/issues/106) [#43](https://github.com/kreuzwerker/terraform-provider-docker/issues/43))

* Adds asc sorting to container ports flattening to fix blinking test.

* Add container healthcheck

* Adds container healthcheck.

* Add capability to not start container (create only)

* Add test

* Adds the docker container start flag. Closes #62. ([#62](https://github.com/kreuzwerker/terraform-provider-docker/issues/62))

* Adds cpu_set to containers. Closes #41 ([#41](https://github.com/kreuzwerker/terraform-provider-docker/issues/41))

* Adds container static IPv4/IPv6 address. Marks network and network_alias as deprecated. Closes #105. ([#105](https://github.com/kreuzwerker/terraform-provider-docker/issues/105))

* Add logs attribute to get container logs when attach option is enabled

* Adds container logs option. Closes #108. ([#108](https://github.com/kreuzwerker/terraform-provider-docker/issues/108))

* Add ssh protocol (copy) (#153). Closes #112 ([#153](https://github.com/kreuzwerker/terraform-provider-docker/issues/153) [#112](https://github.com/kreuzwerker/terraform-provider-docker/issues/112))

* Adds cross-platform support for generic Docker credential helper. (#159) ([#159](https://github.com/kreuzwerker/terraform-provider-docker/issues/159) [#143](https://github.com/kreuzwerker/terraform-provider-docker/issues/143))

* Add support for sysctls (#172) ([#172](https://github.com/kreuzwerker/terraform-provider-docker/issues/172))

* adds container working dir (#181) ([#181](https://github.com/kreuzwerker/terraform-provider-docker/issues/181) [#146](https://github.com/kreuzwerker/terraform-provider-docker/issues/146))

* add container ipc mode. (#182) ([#182](https://github.com/kreuzwerker/terraform-provider-docker/issues/182) [#12](https://github.com/kreuzwerker/terraform-provider-docker/issues/12))

* Add support for group-add (#192) ([#192](https://github.com/kreuzwerker/terraform-provider-docker/issues/192) [#191](https://github.com/kreuzwerker/terraform-provider-docker/issues/191))

* Add `shm_size' attribute for `docker_container' resource. (#190) ([#190](https://github.com/kreuzwerker/terraform-provider-docker/issues/190) [#164](https://github.com/kreuzwerker/terraform-provider-docker/issues/164))

* Add support for readonly containers (#206) ([#206](https://github.com/kreuzwerker/terraform-provider-docker/issues/206) [#203](https://github.com/kreuzwerker/terraform-provider-docker/issues/203))

* adds import for resources (#196) ([#196](https://github.com/kreuzwerker/terraform-provider-docker/issues/196) [#99](https://github.com/kreuzwerker/terraform-provider-docker/issues/99))

* make UID, GID, & mode for secrets and configs configurable (#231) ([#231](https://github.com/kreuzwerker/terraform-provider-docker/issues/231) [#216](https://github.com/kreuzwerker/terraform-provider-docker/issues/216))

* adds config file content as plain string (#232) ([#232](https://github.com/kreuzwerker/terraform-provider-docker/issues/232) [#224](https://github.com/kreuzwerker/terraform-provider-docker/issues/224))

* support to import some docker_container's attributes (#234) ([#234](https://github.com/kreuzwerker/terraform-provider-docker/issues/234))

* supports to update docker_container (#236) ([#236](https://github.com/kreuzwerker/terraform-provider-docker/issues/236))

* allow use of source file instead of content / content_base64 (#240) ([#240](https://github.com/kreuzwerker/terraform-provider-docker/issues/240) [#239](https://github.com/kreuzwerker/terraform-provider-docker/issues/239))

* adds complete support for Docker credential helpers (#253) ([#253](https://github.com/kreuzwerker/terraform-provider-docker/issues/253) [#252](https://github.com/kreuzwerker/terraform-provider-docker/issues/252))

* adds docker Image build feature (#283) ([#283](https://github.com/kreuzwerker/terraform-provider-docker/issues/283))

* conditionally adding port binding (#293). ([#293](https://github.com/kreuzwerker/terraform-provider-docker/issues/293) [#255](https://github.com/kreuzwerker/terraform-provider-docker/issues/255))

* Expose IPv6 properties as attributes


### Fix

* Fix a serious problem when using links.

* Fix Repository attribute in docker client PullOptions for private registries.

* fix resource constraint specs

* Fixing yet more gofmt errors with imports

* Fix typo

* Fix docker test assertions regarding latest tag

* Fix Image Destroy bug. #3609 #3771 ([#3609](https://github.com/kreuzwerker/terraform-provider-docker/issues/3609) [#3771](https://github.com/kreuzwerker/terraform-provider-docker/issues/3771))

* Fix(docs) Correct spelling error in Docker documentation

* Fix #1402 ([#1402](https://github.com/kreuzwerker/terraform-provider-docker/issues/1402))

* Fix Changelog Links Script for docker provider

* Fixing link in README

* Fixing logo

* Fixes layout and notes in docs. (#26) ([#26](https://github.com/kreuzwerker/terraform-provider-docker/issues/26))

* Fixing build and private image

* Fixed test for ulimits on containers

* Fix service flatteners (#66) ([#66](https://github.com/kreuzwerker/terraform-provider-docker/issues/66))

* Fix/map to slice expander (#82) ([#82](https://github.com/kreuzwerker/terraform-provider-docker/issues/82))

* Fix/cert material (#91) ([#91](https://github.com/kreuzwerker/terraform-provider-docker/issues/91) [#86](https://github.com/kreuzwerker/terraform-provider-docker/issues/86) [#14](https://github.com/kreuzwerker/terraform-provider-docker/issues/14))

* fixes ports on containers (#95) ([#95](https://github.com/kreuzwerker/terraform-provider-docker/issues/95) [#8](https://github.com/kreuzwerker/terraform-provider-docker/issues/8) [#89](https://github.com/kreuzwerker/terraform-provider-docker/issues/89) [#73](https://github.com/kreuzwerker/terraform-provider-docker/issues/73))

* Fix other tests as port internal/external are not strings but int

* Fixes bug introduced from merge of #106 ([#106](https://github.com/kreuzwerker/terraform-provider-docker/issues/106))

* Fixes dependencies for old docker client and tests introduced by merge of #49. ([#49](https://github.com/kreuzwerker/terraform-provider-docker/issues/49))

* Fix incorrect indentation for container in docs (#126) ([#126](https://github.com/kreuzwerker/terraform-provider-docker/issues/126))

* Fix container ports issue for asc ordering (#115) ([#115](https://github.com/kreuzwerker/terraform-provider-docker/issues/115))

* Normalize a blank string to 0.0.0.0 (#128) ([#128](https://github.com/kreuzwerker/terraform-provider-docker/issues/128))

* Fix syntax error in docker_service example and make all examples adhere to terraform fmt (#137) ([#137](https://github.com/kreuzwerker/terraform-provider-docker/issues/137))

* Fixes for image pulling and local registry (#143) ([#143](https://github.com/kreuzwerker/terraform-provider-docker/issues/143) [#24](https://github.com/kreuzwerker/terraform-provider-docker/issues/24) [#120](https://github.com/kreuzwerker/terraform-provider-docker/issues/120) [#77](https://github.com/kreuzwerker/terraform-provider-docker/issues/77) [#125](https://github.com/kreuzwerker/terraform-provider-docker/issues/125))

* Fixes for flaky tests (#154) ([#154](https://github.com/kreuzwerker/terraform-provider-docker/issues/154))

* fix website / containers / mount vs mounts (#162) ([#162](https://github.com/kreuzwerker/terraform-provider-docker/issues/162))

* Fix no-op in container when all 'ports' blocks are deleted. (#168) ([#168](https://github.com/kreuzwerker/terraform-provider-docker/issues/168) [#167](https://github.com/kreuzwerker/terraform-provider-docker/issues/167))

* destroy_grace_seconds are considered (#179) ([#179](https://github.com/kreuzwerker/terraform-provider-docker/issues/179) [#174](https://github.com/kreuzwerker/terraform-provider-docker/issues/174))

* service env truncation for multiple delimiters (#193) ([#193](https://github.com/kreuzwerker/terraform-provider-docker/issues/193) [#121](https://github.com/kreuzwerker/terraform-provider-docker/issues/121))

* binary upload as base 64 content (#194) ([#194](https://github.com/kreuzwerker/terraform-provider-docker/issues/194) [#48](https://github.com/kreuzwerker/terraform-provider-docker/issues/48))

* fix service test mount set key

* label for network and volume after improt

* fix sprintf formatter

* replica to 0 in current schema. Closes #221 ([#221](https://github.com/kreuzwerker/terraform-provider-docker/issues/221))

* ports flattening (#233) ([#233](https://github.com/kreuzwerker/terraform-provider-docker/issues/233) [#222](https://github.com/kreuzwerker/terraform-provider-docker/issues/222))

* corrects IPAM config read on the data provider (#229) ([#229](https://github.com/kreuzwerker/terraform-provider-docker/issues/229))

* service endpoint spec flattening

* prevent force recreate of container about some attributes (#269) ([#269](https://github.com/kreuzwerker/terraform-provider-docker/issues/269) [#242](https://github.com/kreuzwerker/terraform-provider-docker/issues/242) [#270](https://github.com/kreuzwerker/terraform-provider-docker/issues/270))

* pins docker registry for tests to v2.7.0

* panic to migrate schema of docker_container from v1 to v2 (#271). Closes #264 ([#271](https://github.com/kreuzwerker/terraform-provider-docker/issues/271) [#264](https://github.com/kreuzwerker/terraform-provider-docker/issues/264))

* port objects with the same internal port but different protocol trigger recreation of container (#274) ([#274](https://github.com/kreuzwerker/terraform-provider-docker/issues/274))

* duplicated buildImage function

* ignores 'remove_volumes' on container import


### Other

* initial commit

* Initial commit. This adds the initial bits of a Docker provider.

* support DOCKER_CERT_PATH

* docker_image acceptance test

* container acceptance tests

* cache client

* make container test better

* ping docker server on startup

* default cert_path to non-nil so input isn't asked

* guard against nil NetworkSettings

* fmt on container resource

* update image sha

* This puts the image parsing code (mostly) back to how it was before. The

* fmt

* When linking to other containers, introduce a slight delay; this lets

* As discussed on the issue, remove the hard-coded delay on startup in

* [tests] change images

* Gofmt change for resource docker_image test

* removed extra parentheses

* fix image test

* entrypoint support for docker_container resource

* restart policy support for docker_container

* add basic runtime constraints to docker_container

* add label support to docker container resource

* support for log driver + config in docker container

* include hostconfig when creating docker_container

* Merge pull request #3761 from ryane/f-provider-docker-improvements ([#3761](https://github.com/kreuzwerker/terraform-provider-docker/issues/3761))

* Refer to a tag instead of latest

* locate container via ID not name ([#3364](https://github.com/kreuzwerker/terraform-provider-docker/issues/3364))

* Convert v to string

* Merge branch 'docker_network' of https://github.com/ColinHebert/terraform into ColinHebert-docker_network

* Fix flaky integration tests

* Add hosts parameter for containers

* Inline ports and volumes schemas for consistency

* Merge branch 'docker-extra-hosts' of https://github.com/paulbellamy/terraform into paulbellamy-docker-extra-hosts

* Tweak and test `host_entry`

* Add `docker_volume` resource

* Mount named volumes in containers

* Catch potential custom network errors in docker

* remove extra parenthesis

* Change default DOCKER_HOST value, fixes #4923 ([#4923](https://github.com/kreuzwerker/terraform-provider-docker/issues/4923))

* Use built-in schema.HashString.

* Merge pull request #5046 from tpounds/use-built-in-schema-string-hash ([#5046](https://github.com/kreuzwerker/terraform-provider-docker/issues/5046))

* Stop providing the hostConfig while starting the container

* #2417 Add support for restart policy unless-stopped ([#2417](https://github.com/kreuzwerker/terraform-provider-docker/issues/2417))

* #5298 Add support for docker run --user option ([#5298](https://github.com/kreuzwerker/terraform-provider-docker/issues/5298))

* Provider Docker: (#6376) ([#6376](https://github.com/kreuzwerker/terraform-provider-docker/issues/6376))

* don't crash with empty commands ([#6409](https://github.com/kreuzwerker/terraform-provider-docker/issues/6409))

* Fixing the Docker Container Mount Test

* Docker DNS Setting Enhancements (#7392) ([#7392](https://github.com/kreuzwerker/terraform-provider-docker/issues/7392))

* Docker documentation and additional test message (#7412) ([#7412](https://github.com/kreuzwerker/terraform-provider-docker/issues/7412))

* Added docker_registry_image data source (#7000) ([#7000](https://github.com/kreuzwerker/terraform-provider-docker/issues/7000))

* Fixes for docker_container host object and documentation (#9367) ([#9367](https://github.com/kreuzwerker/terraform-provider-docker/issues/9367) [#9350](https://github.com/kreuzwerker/terraform-provider-docker/issues/9350) [#9350](https://github.com/kreuzwerker/terraform-provider-docker/issues/9350))

* authentication via values instead of files (#10151) ([#10151](https://github.com/kreuzwerker/terraform-provider-docker/issues/10151))

* Upload files into container before first start (#9520) ([#9520](https://github.com/kreuzwerker/terraform-provider-docker/issues/9520))

* fix regression, cert_path stop working (#10754) (#10801) ([#10754](https://github.com/kreuzwerker/terraform-provider-docker/issues/10754) [#10801](https://github.com/kreuzwerker/terraform-provider-docker/issues/10801))

* Add network create --internal flag support (#10932) ([#10932](https://github.com/kreuzwerker/terraform-provider-docker/issues/10932))

* Add support for a list of pull_triggers within the docker_image resource. (#10845) ([#10845](https://github.com/kreuzwerker/terraform-provider-docker/issues/10845))

* added support for linux capabilities (#12045) ([#12045](https://github.com/kreuzwerker/terraform-provider-docker/issues/12045) [#11623](https://github.com/kreuzwerker/terraform-provider-docker/issues/11623))

* provider/docker network alias (#14710) ([#14710](https://github.com/kreuzwerker/terraform-provider-docker/issues/14710))

* Transfer docker provider

* Merge branch 'master' of /Users/jake/terraform

* Initial transfer of provider code

* Updating Makefile + Add gitignore

* docker docs

* note on docker

* Merge pull request #1564 from nickryand/docker_links ([#1564](https://github.com/kreuzwerker/terraform-provider-docker/issues/1564))

* The docker-image resource expects name, not image

* Update container.html.markdown

* Example for the command arg on docker_container. ([#3011](https://github.com/kreuzwerker/terraform-provider-docker/issues/3011))

* Merge pull request #3383 from apparentlymart/docker-container-command-docs ([#3383](https://github.com/kreuzwerker/terraform-provider-docker/issues/3383))

* entrypoint support for docker_container resource

* restart policy support for docker_container

* add basic runtime constraints to docker_container

* add label support to docker container resource

* support for log driver + config in docker container

* Merge branch 'docker_network' of https://github.com/ColinHebert/terraform into ColinHebert-docker_network

* Add hosts parameter for containers

* Merge branch 'docker-extra-hosts' of https://github.com/paulbellamy/terraform into paulbellamy-docker-extra-hosts

* Tweak and test `host_entry`

* Add `docker_volume` resource

* Mount named volumes in containers

* Update documentation

* #2417 Add support for restart policy unless-stopped ([#2417](https://github.com/kreuzwerker/terraform-provider-docker/issues/2417))

* #5298 Add support for docker run --user option ([#5298](https://github.com/kreuzwerker/terraform-provider-docker/issues/5298))

* Provider Docker: (#6376) ([#6376](https://github.com/kreuzwerker/terraform-provider-docker/issues/6376))

* Docker documentation and additional test message (#7412) ([#7412](https://github.com/kreuzwerker/terraform-provider-docker/issues/7412))

* Docs sweep for lists & maps

* Update index.html.markdown

* Update index.html.markdown

* Add alternative to cert_path

* Fixes for docker_container host object and documentation (#9367) ([#9367](https://github.com/kreuzwerker/terraform-provider-docker/issues/9367) [#9350](https://github.com/kreuzwerker/terraform-provider-docker/issues/9350) [#9350](https://github.com/kreuzwerker/terraform-provider-docker/issues/9350))

* authentication via values instead of files (#10151) ([#10151](https://github.com/kreuzwerker/terraform-provider-docker/issues/10151))

* Upload files into container before first start (#9520) ([#9520](https://github.com/kreuzwerker/terraform-provider-docker/issues/9520))

* Add network create --internal flag support (#10932) ([#10932](https://github.com/kreuzwerker/terraform-provider-docker/issues/10932))

* Add support for a list of pull_triggers within the docker_image resource. (#10845) ([#10845](https://github.com/kreuzwerker/terraform-provider-docker/issues/10845))

* Run `terraform fmt` on code examples (#12075) ([#12075](https://github.com/kreuzwerker/terraform-provider-docker/issues/12075))

* added support for linux capabilities (#12045) ([#12045](https://github.com/kreuzwerker/terraform-provider-docker/issues/12045) [#11623](https://github.com/kreuzwerker/terraform-provider-docker/issues/11623))

* Removing the note on docker provider about Terraform (#12676) ([#12676](https://github.com/kreuzwerker/terraform-provider-docker/issues/12676) [#12670](https://github.com/kreuzwerker/terraform-provider-docker/issues/12670))

* Massively add HCL source tag in docs Markdown files

* provider/docker network alias (#14710) ([#14710](https://github.com/kreuzwerker/terraform-provider-docker/issues/14710))

* Transfer docker provider website

* Merge branch 'master' of /Users/jake/terraform

* Transfer of provider website docs

* Transfer docker provider

* Merge branch 'master' of /home/ubuntu/terraform-vendor

* Transfer of provider code

* Updating Makefile + Add gitignore

* Update CHANGELOG.md

* v0.1.0

* Cleanup after v0.1.0 release

* Simplifying the GNUMakefile

* Ignore github.com/hashicorp/terraform/backend

* github.com/hashicorp/terraform/...@v0.10.0

* Merge pull request #18 from terraform-providers/vendor-tf-0.10 ([#18](https://github.com/kreuzwerker/terraform-provider-docker/issues/18))

* Correct git paths in the README.md file

* Correct comment in `docker_network` documentation

* Merge pull request #23 from JamesLaverack/patch-1 ([#23](https://github.com/kreuzwerker/terraform-provider-docker/issues/23))

* Make CoC and support channels more visible

* Update CHANGELOG.md

* v0.1.1

* Cleanup after v0.1.1 release

* add prefix 'library' only to official images in the path (#27) ([#27](https://github.com/kreuzwerker/terraform-provider-docker/issues/27))

* Update go-dockerclient

* Updated dockerclient to bf3bc17bb (#46) ([#46](https://github.com/kreuzwerker/terraform-provider-docker/issues/46))

* Updated private registry port to 15000 for fix teamcity build.

* Using absolute paths instead of relative in test scripts

* updated test script to clean up properly

* added 3rd test image and made build more generic

* Travis build uses docker version 18.03.0 to fix the build (#57) ([#57](https://github.com/kreuzwerker/terraform-provider-docker/issues/57))

* [ci skip] Updated CHANGELOG

* Add website + website-test targets

* Merge pull request #60 from terraform-providers/f-make-website ([#60](https://github.com/kreuzwerker/terraform-provider-docker/issues/60))

* correct provider organization & missing repository name

* [ci skip] update changelog

* Marks the links property as deprecated

* Merge pull request #47 from captn3m0/docker-link-warning ([#47](https://github.com/kreuzwerker/terraform-provider-docker/issues/47))

* Update CHANGELOG.md to include #47 ([#47](https://github.com/kreuzwerker/terraform-provider-docker/issues/47))

* Update/docker-18-03-1 (#68) ([#68](https://github.com/kreuzwerker/terraform-provider-docker/issues/68))

* Update CHANGELOG.md

* Update CHANGELOG.md

* update docker deps to 65bd038

* Migrate/docker-client (#70) ([#70](https://github.com/kreuzwerker/terraform-provider-docker/issues/70) [#32](https://github.com/kreuzwerker/terraform-provider-docker/issues/32))

* v1.0.0

* Cleanup after v1.0.0 release

* merge master

* merge vendor

* Merge branch 'master' of github.com:terraform-providers/terraform-provider-docker

* Update CHANGELOG.md

* v1.0.1

* Cleanup after v1.0.1 release

* v1.0.2

* Cleanup after v1.0.2 release

* [ci skip] updates CHANGELOG for windows support

* Image can be pulled with its repo digest (#97) ([#97](https://github.com/kreuzwerker/terraform-provider-docker/issues/97) [#79](https://github.com/kreuzwerker/terraform-provider-docker/issues/79))

* [ci skip] Fixes PR links in CHANGELOG

* v1.0.3

* Cleanup after v1.0.3 release

* Support for random external port for containers (#103) ([#103](https://github.com/kreuzwerker/terraform-provider-docker/issues/103) [#102](https://github.com/kreuzwerker/terraform-provider-docker/issues/102))

* v1.0.4

* Cleanup after v1.0.4 release

* [ci skip] updates CHANGELOG

* Container network fixes (#104) ([#104](https://github.com/kreuzwerker/terraform-provider-docker/issues/104) [#50](https://github.com/kreuzwerker/terraform-provider-docker/issues/50) [#9](https://github.com/kreuzwerker/terraform-provider-docker/issues/9) [#98](https://github.com/kreuzwerker/terraform-provider-docker/issues/98) [#107](https://github.com/kreuzwerker/terraform-provider-docker/issues/107))

* updates CHANGELOG

* Update doc

* bla

* Update doc

* Merges master

* cpuset added

* fmt

* Merge branch 'd-cpuset-added' of git://github.com/sunthera/terraform-provider-docker into sunthera/d-cpuset-added

* Merge branch 'sunthera/d-cpuset-added'

* Simplify the image options parser.

* Simplifies the image options parser. Closes #49. ([#49](https://github.com/kreuzwerker/terraform-provider-docker/issues/49))

* Merge branch 'mprihoda-wip/registry-parser'

* Merge branch 'bhuisgen-feature/docker-container-ipv6'

* Update tests

* Update doc

* Merge branch 'bhuisgen-feature/container-attach-logs'

* v1.1.0

* Cleanup after v1.1.0 release

* Updates network_advanced documentation for containers. Closes #109 ([#109](https://github.com/kreuzwerker/terraform-provider-docker/issues/109))

* [ci skip] updates CHANGELOG

* Update service.html fixed typo `tmpf_options` (#122) ([#122](https://github.com/kreuzwerker/terraform-provider-docker/issues/122))

* Updates changelog for docs corrections.

* Merge pull request #135 from terraform-providers/t-simplify-dockerfile ([#135](https://github.com/kreuzwerker/terraform-provider-docker/issues/135))

* updates CHANGELOG for v1.1.1

* v1.1.1

* Cleanup after v1.1.1 release

* provider: Ensured Go 1.11 in TravisCI and README

* deps: use go modules for dep mgmt

* deps: github.com/hashicorp/terraform@sdk-v0.11-with-go-modules

* remove turn modules off for gox installation

* Merge pull request #134 from terraform-providers/go-modules-2019-03-01 ([#134](https://github.com/kreuzwerker/terraform-provider-docker/issues/134))

* provider: Require Go 1.11 in TravisCI and README

* Upgrade to go 1.11

* Update to docker to 18.09 (#152) ([#152](https://github.com/kreuzwerker/terraform-provider-docker/issues/152) [#114](https://github.com/kreuzwerker/terraform-provider-docker/issues/114))

* updates changelog for v1.2.0

* updates docker api version to 1.39 and adapts changelog

* [ci skip]: Updates missing docs for changes of #147 ([#147](https://github.com/kreuzwerker/terraform-provider-docker/issues/147))

* v1.2.0

* Cleanup after v1.2.0 release

* Refactors test setup (#156) ([#156](https://github.com/kreuzwerker/terraform-provider-docker/issues/156))

* Update to Terraform 0.12 (#150). Closes #144 ([#150](https://github.com/kreuzwerker/terraform-provider-docker/issues/150) [#144](https://github.com/kreuzwerker/terraform-provider-docker/issues/144))

* updates CHANGELOG for v2.0.0

* v2.0.0

* Cleanup after v2.0.0 release

* Updates the docs (#165). Closes  #158 ([#165](https://github.com/kreuzwerker/terraform-provider-docker/issues/165) [#158](https://github.com/kreuzwerker/terraform-provider-docker/issues/158) [#147](https://github.com/kreuzwerker/terraform-provider-docker/issues/147) [#153](https://github.com/kreuzwerker/terraform-provider-docker/issues/153))

* [ci skip] updates CHANGELOG for v2.1.0

* v2.1.0

* Cleanup after v2.1.0 release

* v2.1.1

* Cleanup after v2.1.1 release

* Using APIVersion negotiation instead of fixed version (#177) ([#177](https://github.com/kreuzwerker/terraform-provider-docker/issues/177) [#137](https://github.com/kreuzwerker/terraform-provider-docker/issues/137))

* updates CHANGELOG for v2.2.0

* v2.2.0

* remove usage of config pkg (#183) ([#183](https://github.com/kreuzwerker/terraform-provider-docker/issues/183))

* [ci skip] updates CHANGELOG v2.3.0

* v2.3.0

* Cleanup after v2.3.0 release

* Remove duplicate start_period in docker_service documentation (#189) ([#189](https://github.com/kreuzwerker/terraform-provider-docker/issues/189))

* Calculate digest when missing from registry response headers (#188) ([#188](https://github.com/kreuzwerker/terraform-provider-docker/issues/188) [#186](https://github.com/kreuzwerker/terraform-provider-docker/issues/186))

* [ci skip] updates CHANGELOG v2.4.0

* v2.4.0

* Cleanup after v2.4.0 release

* Move to standalone plugin SDK (#200) ([#200](https://github.com/kreuzwerker/terraform-provider-docker/issues/200) [#197](https://github.com/kreuzwerker/terraform-provider-docker/issues/197))

* Updated logdrivers to match docker officially supported options (#207) ([#207](https://github.com/kreuzwerker/terraform-provider-docker/issues/207) [#204](https://github.com/kreuzwerker/terraform-provider-docker/issues/204))

* CI restructuring and migration to golang 1.13 (#202) ([#202](https://github.com/kreuzwerker/terraform-provider-docker/issues/202) [#198](https://github.com/kreuzwerker/terraform-provider-docker/issues/198))

* Remove logging drivers white-list (#209) ([#209](https://github.com/kreuzwerker/terraform-provider-docker/issues/209) [#207](https://github.com/kreuzwerker/terraform-provider-docker/issues/207) [#208](https://github.com/kreuzwerker/terraform-provider-docker/issues/208))

* [ci-skip] updates CHANGELOG for v2.5.0

* [ci skip] update CHANGELOG next release version

* v2.5.0

* Cleanup after v2.5.0 release

* Correct mounts block name (#218) ([#218](https://github.com/kreuzwerker/terraform-provider-docker/issues/218))

* [ci-skip] updates CHANGELOG for v2.6.0

* v2.6.0

* Cleanup after v2.6.0 release

* trying something different

* woops

* use %v not %s

* specify labels are optional

* try straight indices

* get a look at all the Attributes

* try this again?

* try this!

* skip the size var

* migrate the container resource

* secret and network cleanup

* volume

* service

* some more migration

* re-run travis, possible flaky test

* some debugging

* Merge branch 'xf/labels-iface' of git://github.com/xanderflood/terraform-provider-docker into xanderflood-xf/labels-iface

* Merge branch 'xanderflood-xf/labels-iface'

* allow zero replicas

* Merge branch 'xf/allow-zero-replicas' of git://github.com/xanderflood/terraform-provider-docker into xanderflood-xf/allow-zero-replicas

* Merge branch 'xanderflood-xf/allow-zero-replicas'

* Wait for state until endpoint spec is exposed

* Set TF_LOG=DEBUG

* Merge branch 'debug-issue-237' of https://github.com/suzuki-shunsuke/terraform-provider-docker into suzuki-shunsuke-debug-issue-237

* Merge branch 'suzuki-shunsuke-debug-issue-237'

* [ci-skip] updates CHANGELOG for v2.7.0

* v2.7.0

* Cleanup after v2.7.0 release

* [ci-skip] updates CHANGELOG for v2.7.1

* v2.7.1

* Cleanup after v2.7.1 release

* Set `Computed: true` and separate files of resourceDockerContainerV1 (#272) ([#272](https://github.com/kreuzwerker/terraform-provider-docker/issues/272))

* [ci-skip] updates CHANGELOG for v2.7.2

* v2.7.2

* Cleanup after v2.7.2 release

* Merge branch 'akomic-image_build' into master

* added docker_registry_image

* added documentation

* removed jsonmessage dependency

* removed assert dependency

* added error handling if context file not found

* Merge branch 'feature/resource-docker_registry_image' of git://github.com/edgarpoce/terraform-provider-docker into edgarpoce-feature/resource-docker_registry_image

* Merge branch 'edgarpoce-feature/resource-docker_registry_image' into master

* #250 no errors if auth config incomplete ([#250](https://github.com/kreuzwerker/terraform-provider-docker/issues/250))

* Merge branch 'bugfix/support_missing_auth_in_provider' of git://github.com/edgarpoce/terraform-provider-docker into edgarpoce-bugfix/support_missing_auth_in_provider

* Merge branch 'edgarpoce-bugfix/support_missing_auth_in_provider' into master

* Merge branch 'feat/ipv6-attrs' of git://github.com/ellsclytn/terraform-provider-docker into ellsclytn-feat/ipv6-attrs

* Merge branch 'ellsclytn-feat/ipv6-attrs' into master

* Merge branch 'master' of git://github.com/juliosueiras/terraform-provider-docker into juliosueiras-master

* Merge branch 'juliosueiras-master' into master

* Update service.html.markdown

* Merge branch 'patch-1' of git://github.com/motti24/terraform-provider-docker into motti24-patch-1

* Merge branch 'motti24-patch-1' into master


### Refactor

* refactor migration code and fix a couple tests


### Test

* Simplify Dockerfile(s)

* Skip test if swap limit isn't available (#136) ([#136](https://github.com/kreuzwerker/terraform-provider-docker/issues/136))

* tests for label migration





---

# README

**File:** `README.md`
**Tipo:** `.md`
**Dimensione:** 7.2 KB
**Ultima modifica:** 16/06/2026 11:53

---

<a href="https://docker.com">
    <img src="https://raw.githubusercontent.com/kreuzwerker/terraform-provider-docker/master/assets/docker-logo.png" alt="Docker logo" title="Docker" align="right" height="100" />
</a>
<a href="https://terraform.io">
    <img src="https://raw.githubusercontent.com/kreuzwerker/terraform-provider-docker/master/assets/terraform-logo.png" alt="Terraform logo" title="Terraform" align="right" height="100" />
</a>

# Terraform Provider for Docker

[![Release](https://img.shields.io/github/v/release/kreuzwerker/terraform-provider-docker)](https://github.com/kreuzwerker/terraform-provider-docker/releases)
[![Installs](https://img.shields.io/badge/dynamic/json?logo=terraform&label=installs&query=$.data.attributes.downloads&url=https%3A%2F%2Fregistry.terraform.io%2Fv2%2Fproviders%2F713)](https://registry.terraform.io/providers/kreuzwerker/docker)
[![Registry](https://img.shields.io/badge/registry-doc%40latest-lightgrey?logo=terraform)](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/kreuzwerker/terraform-provider-docker/blob/main/LICENSE)  
[![Acc Tests](https://github.com/kreuzwerker/terraform-provider-docker/actions/workflows/acc-test.yaml/badge.svg?branch=master)](https://github.com/kreuzwerker/terraform-provider-docker/actions/workflows/acc-test.yaml)
[![golangci-lint](https://github.com/kreuzwerker/terraform-provider-docker/actions/workflows/golangci-lint.yaml/badge.svg?branch=master)](https://github.com/kreuzwerker/terraform-provider-docker/actions/workflows/golangci-lint.yaml)
[![Go Report Card](https://goreportcard.com/badge/github.com/kreuzwerker/terraform-provider-docker)](https://goreportcard.com/report/github.com/kreuzwerker/terraform-provider-docker)

Sponsored by [Coder](https://coder.com/)

## What You Can Manage With This Provider

This provider covers more than basic Docker images and containers. With Terraform, you can manage:

* Compose applications with [`docker_compose`](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs/resources/compose)
* Image builds and registry workflows with [`docker_image`](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs/resources/image), [`docker_registry_image`](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs/resources/registry_image), and [`docker_tag`](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs/resources/tag)
* Buildx builders for advanced multi-platform builds with [`docker_buildx_builder`](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs/resources/buildx_builder)
* Swarm services with [`docker_service`](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs/resources/service)
* Runtime resources such as [`docker_container`](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs/resources/container), [`docker_network`](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs/resources/network), and [`docker_volume`](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs/resources/volume)
* Supporting platform objects like [`docker_config`](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs/resources/config), [`docker_secret`](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs/resources/secret), and [`docker_plugin`](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs/resources/plugin)
* Operational actions such as [`docker_exec`](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs/actions/exec), [`docker_image_import`](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs/actions/image_import), [`docker_image_load`](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs/actions/image_load), [`docker_image_save`](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs/actions/image_save), [`docker_container_export`](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs/actions/container_export) and [`docker_system_prune`](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs/actions/system_prune), 

Available data sources include images, image tags and manifests, containers, networks, plugins, and container logs. See the full [provider documentation](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs) for the complete resource and data source list.

## Documentation

The documentation for the provider is available on the [Terraform Registry](https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs).
You need at least Terraform `1.1.5` to use this provider.

Migration guides:
* Do you want to migrate from `v3.x` to `v4.x`? Please read the [V3 - V4 migration guide](docs/v3_v4_migration.md)
* Do you want to migrate from `v2.x` to `v3.x`? Please read the [V2 - V3 migration guide](docs/v2_v3_migration.md)

## Example usage

Take a look at the examples in the [documentation](https://registry.terraform.io/providers/kreuzwerker/docker/4.4.0/docs) of the registry
or use the following example:


```hcl
# Set the required provider and versions
terraform {
  required_providers {
    # We recommend pinning to the specific version of the Docker Provider you're using
    # since new versions are released frequently
    docker = {
      source  = "kreuzwerker/docker"
      # or if you want to pull from opentfu
      source = "registry.opentofu.org/kreuzwerker/docker"
      version = "4.4.0"
    }
  }
}

# Configure the docker provider
provider "docker" {
}

# Create a docker image resource
# -> docker pull nginx:latest
resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = true
}

# Create a docker container resource
# -> same as 'docker run --name nginx -p8080:80 -d nginx:latest'
resource "docker_container" "nginx" {
  name    = "nginx"
  image   = docker_image.nginx.image_id

  ports {
    external = 8080
    internal = 80
  }
}

# Or create a service resource
# -> same as 'docker service create -d -p 8081:80 --name nginx-service --replicas 2 nginx:latest'
resource "docker_service" "nginx_service" {
  name = "nginx-service"
  task_spec {
    container_spec {
      image = docker_image.nginx.repo_digest
    }
  }

  mode {
    replicated {
      replicas = 2
    }
  }

  endpoint_spec {
    ports {
      published_port = 8081
      target_port    = 80
    }
  }
}
```

## Building The Provider

[Go](https://golang.org/doc/install) 1.18.x (to build the provider plugin)


```sh
$ git clone git@github.com:kreuzwerker/terraform-provider-docker
$ make build
```

## Contributing

The Terraform Docker Provider is the work of many of contributors. We appreciate your help!

To contribute, please read the contribution guidelines: [Contributing to Terraform - Docker Provider](CONTRIBUTING.md)

## License

The Terraform Provider Docker is available to everyone under the terms of the Mozilla Public License Version 2.0. [Take a look the LICENSE file](LICENSE).


## Stargazers over time

[![Stargazers over time](https://starchart.cc/kreuzwerker/terraform-provider-docker.svg)](https://starchart.cc/kreuzwerker/terraform-provider-docker)

## Sponsors

[![Coder](https://avatars.githubusercontent.com/u/95932066?s=100&v=2)](https://coder.com/)


---

# db

**File:** `db.json`
**Tipo:** `.json`
**Dimensione:** 0.7 KB
**Ultima modifica:** 16/06/2026 11:51

---

{
  "posts": [
    {
      "thread": 1,
      "text": "That last goal was awesome!",
      "user": 4
    },
    {
      "thread": 1,
      "text": "Yes, the way the ball swerved... What talent!",
      "user": 2
    },
    {
      "thread": 2,
      "text": "I have to try their tarts!",
      "user": 3
    },
    {
      "thread": 2,
      "text": "I'm planning to stop by in the morning to try their croissants.",
      "user": 2
    },
    {
      "thread": 2,
      "text": "I could go for a chocolate eclair!",
      "user": 1
    },
    {
      "thread": 3,
      "text": "I need a new acoustic guitar at a good price.",
      "user": 1
    }
  ]
}



---

# package

**File:** `package.json`
**Tipo:** `.json`
**Dimensione:** 0.1 KB
**Ultima modifica:** 16/06/2026 11:51

---

{
  "dependencies": {
    "koa": "^1.2.5",
    "koa-router": "^5.4.0"
  },
  "scripts": {
    "start": "node server.js"
  }
}



---

# server

**File:** `server.js`
**Tipo:** `.js`
**Dimensione:** 0.9 KB
**Ultima modifica:** 16/06/2026 11:51

---

const app = require('koa')();
const router = require('koa-router')();
const db = require('./db.json');

// Log requests
app.use(function *(next){
  const start = new Date;
  yield next;
  const ms = new Date - start;
  console.log('%s %s - %s', this.method, this.url, ms);
});

router.get('/api/posts/in-thread/:threadId', function *() {
  const id = parseInt(this.params.threadId);
  this.body = db.posts.filter((post) => post.thread == id);
});

router.get('/api/posts/by-user/:userId', function *() {
  const id = parseInt(this.params.userId);
  this.body = db.posts.filter((post) => post.user == id);
});

router.get('/api/', function *() {
  this.body = "API ready to receive requests";
});

router.get('/', function *() {
  this.body = "Ready to receive requests";
});

app.use(router.routes());
app.use(router.allowedMethods());

app.listen(3000);

console.log('Worker started');



---

# README

**File:** `README.md`
**Tipo:** `.md`
**Dimensione:** 2.1 KB
**Ultima modifica:** 16/06/2026 11:51

---

# Terraform/OpenTofu – Microservices Lab

Questo repository contiene un semplice esercizio su **microservizi** basato su **OpenTofu**.

Sono presenti tre microservizi indipendenti:
- `users`
- `threads`
- `post`

Ogni microservizio espone una **API REST** ed è eseguito in un **container Docker**.
I 3 container rappresentano servizi separati (users, threads, posts) tipici di una architettura microservizi REST.  
Ogni servizio espone un’API HTTP su porta 3000 e gestisce una parte indipendente del dominio applicativo.  

Ogni servizio è un’app Node.js containerizzata con un Dockerfile e buildata come immagine separata.  
I container vengono eseguiti da Terraform usando il provider Docker, con porte mappate (3001–3003) e rete comune.  

I 3 container insieme simulano una mini applicazione di social network (tipo Twitter / Threads / Reddit light).  

users → gestisce gli utenti (chi sei)  
threads → gestisce le discussioni (topic / conversazioni)  
posts → gestisce i messaggi (contenuti dentro le discussioni)  

Esattamente come nei social reali:  
- utente crea thread  
- nel thread ci sono i post  

---

## Prerequisiti
- Docker
- OpenTofu

Verifica:

~$ docker --version  
~$ tofu --version

## Avvio
Clona il repository:
~$ git clone https://github.com/paolobelloni-its/microservices.git  
~$ cd microservices  
La cartella microservices contiene il file main.tf e altre 3 cartelle, ciascuna con dentro un Dockerfile.  

Lanciare i container: spostarsi nella cartella che contiene il file main.tf 
~$ tofu init  
~$ tofu plan  
~$ tofu apply    

Verificare che i container siano attivi:  
~$ docker ps  

## Uso delle API  
~$ curl http://localhost:3001/  
~$ curl http://localhost:3001/api/users  
~$ curl http://localhost:3001/api/users/1  

~$ curl http://localhost:3002/  
~$ curl http://localhost:3002/api/threads/  
~$ curl http://localhost:3002/api/threads/1  

~$ curl http://localhost:3003/  
~$ curl http://localhost:3003/api/posts/by-user/1  
~$ curl http://localhost:3003/api/posts/in-thread/1  

## Arrestare i container  
~$ tofu destroy



---

# db

**File:** `db.json`
**Tipo:** `.json`
**Dimensione:** 0.3 KB
**Ultima modifica:** 16/06/2026 11:51

---

{
 "threads": [
    {
      "id": 1,
      "title": "Did you see the Brazil game?",
      "createdBy": 4
    },
    {
      "id": 2,
      "title": "New French bakery opening in the neighborhood tomorrow",
      "createdBy": 3
    },
    {
      "id": 3,
      "title": "In search of a new guitar",
      "createdBy": 1
    }
  ]
}



---

# package

**File:** `package.json`
**Tipo:** `.json`
**Dimensione:** 0.1 KB
**Ultima modifica:** 16/06/2026 11:51

---

{
  "dependencies": {
    "koa": "^1.2.5",
    "koa-router": "^5.4.0"
  },
  "scripts": {
    "start": "node server.js"
  }
}



---

# server

**File:** `server.js`
**Tipo:** `.js`
**Dimensione:** 0.8 KB
**Ultima modifica:** 16/06/2026 11:51

---

const app = require('koa')();
const router = require('koa-router')();
const db = require('./db.json');

// Log requests
app.use(function *(next){
  const start = new Date;
  yield next;
  const ms = new Date - start;
  console.log('%s %s - %s', this.method, this.url, ms);
});

router.get('/api/threads', function *() {
  this.body = db.threads;
});

router.get('/api/threads/:threadId', function *() {
  const id = parseInt(this.params.threadId);
  this.body = db.threads.find((thread) => thread.id == id);
});

router.get('/api/', function *() {
  this.body = "API ready to receive requests";
});

router.get('/', function *() {
  this.body = "Ready to receive requests";
});

app.use(router.routes());
app.use(router.allowedMethods());

app.listen(3000);

console.log('Worker started');



---

# db

**File:** `db.json`
**Tipo:** `.json`
**Dimensione:** 0.5 KB
**Ultima modifica:** 16/06/2026 11:51

---

{
  "users": [
    {
      "id": 1,
      "username": "marceline",
      "name": "Marceline Singer",
      "bio": "Cyclist, musician"
    },
    {
      "id": 2,
      "username": "finn",
      "name": "Finn Alberts",
      "bio": "Adventurer and hero, defender of good"
    },
    {
      "id": 3,
      "username": "pb",
      "name": "Paul Barium",
      "bio": "Scientist, cake lover"
    },
    {
      "id": 4,
      "username": "jake",
      "name": "Jake Storm",
      "bio": "Soccer fan, sky diver"
    }
  ]
}



---

# package

**File:** `package.json`
**Tipo:** `.json`
**Dimensione:** 0.1 KB
**Ultima modifica:** 16/06/2026 11:51

---

{
  "dependencies": {
    "koa": "^1.2.5",
    "koa-router": "^5.4.0"
  },
  "scripts": {
    "start": "node server.js"
  }
}



---

# server

**File:** `server.js`
**Tipo:** `.js`
**Dimensione:** 0.8 KB
**Ultima modifica:** 16/06/2026 11:51

---

const app = require('koa')();
const router = require('koa-router')();
const db = require('./db.json');

// Log requests
app.use(function *(next){
  const start = new Date;
  yield next;
  const ms = new Date - start;
  console.log('%s %s - %s', this.method, this.url, ms);
});

router.get('/api/users', function *(next) {
  this.body = db.users;
});

router.get('/api/users/:userId', function *(next) {
  const id = parseInt(this.params.userId);
  this.body = db.users.find((user) => user.id == id);
});

router.get('/api/', function *() {
  this.body = "API ready to receive requests";
});

router.get('/', function *() {
  this.body = "Ready to receive requests";
});

app.use(router.routes());
app.use(router.allowedMethods());

app.listen(3000);

console.log('Worker started');



---

# VirtCSP - Scheda 1 - Openstack

**File:** `VirtCSP - Scheda 1 - Openstack.pdf`
**Tipo:** `.pdf`
**Dimensione:** 259.4 KB
**Ultima modifica:** 02/07/2026 09:25

---

 
 
C2 General 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
 
DOCENTE Paolo Belloni 
Unità Formativa Sistemi di Virtualizzazione 
Argomento Scheda 1 – Openstack CPU, RAM e rete  

2 
 
L’obiettivo è comprendere il comportamento reale delle risorse di sistema 
all’interno di una VM.  
 
1. Accesso alla VM tramite Floating IP e SSH  
Quando una VM viene creata in OpenStack, riceve un indirizzo IP privato (es. 
10.0.0.x). Questo indirizzo è valido solo all’interno della rete virtuale e non è 
raggiungibile. Per accedere da remoto devi quindi assegnare un Floating IP.  
OBIETTIVO  
Collegarsi alla VM da remoto comprendendo la differenza tra rete privata e 
accesso pubblico.  
 Passo 1 — Creazione Floating IP:  
- Aprire Horizon  
- Andare in Project → Network → Floating IP  
- Cliccare ‘Allocate IP to Project’  
RISULTATO: viene assegnato un IP pubblico.  
 
Passo 2 — Associazione IP:  
- Cliccare ‘Associate’  
- Selezionare la VM e la porta  
RISULTATO: la VM ottiene un IP pubblico.  
 
Passo 3 — Verifica Security Group:  
- Abilitare porta TCP 22  
RISULTATO: SSH permesso.  
 
Passo 4 — Connessione:  
ssh ubuntu@IP-PUBBLICO -i mykey.pem  
mykey.pem viene generato quando si crea istanza: è fondamentale salvare 
la chiave in locale e posizionarsi nella cartella che contiene il file .pem 
quando si fa ssh. 

3 
 
RISULTATO: accesso alla shell Linux.  
INTERPRETAZIONE: senza Floating IP una VM cloud non è raggiungibile 
dall’esterno. 
 
2. Analisi della CPU  
Di seguito alcune considerazioni sulla gestione della CPU da parte di 
Openstack. Si ricorda che Openstack lavora ad un livello più alto rispetto 
l’hypervisor. 
Passo 1 — Identificare CPU:  
cat /proc/cpuinfo  
RISULTATO: numero di vCPU presenti.  
INTERPRETAZIONE: rappresentano le CPU virtuali disponibili.  
Esegui il comando cat /proc/cpuinfo. Questo file contiene informazioni 
dettagliate sulla CPU. Conta quante volte compare la voce 'processor': 
quella è la quantità di CPU virtuali assegnate alla macchina.  
 
Passo 2 — Monitoraggio:  
htop  
OSSERVARE: barre CPU e colori.  
INTERPRETAZIONE:  
- Verde: utilizzo da processi  
- Rosso: sistema  
- Giallo: attesa I/O  
Avvia htop per monitorare la CPU in tempo reale. Osserva le barre colorate: il 
verde indica lavoro eseguito dalle applicazioni, il rosso attività del sistema e il 
giallo eventuale attesa di risorse.  
 
Passo 3 — Generare carico:  
stress --cpu 4 &  
jobs  
RISULTATO: vengono creati processi CPU.  
 
Passo 4 — Osservazione:  
htop  

4 
 
RISULTATO: CPU al 100%.  
INTERPRETAZIONE: più processi competono per CPU.  
Genera carico con stress --cpu 4 &. Ora osserva di nuovo htop: vedrai le CPU 
completamente occupate. Questo significa che i processi stanno 
competendo per la CPU.  
 
Passo 5 — Load average:  
uptime  
RISULTATO: load > numero CPU.  
INTERPRETAZIONE: coda di processi in attesa.  
Usa uptime per leggere il valore 'load average'. Se il valore supera il numero 
di CPU disponibili, significa che il sistema è sovraccarico.  
 
3. Analisi della Memoria  
Esegui free -m per vedere lo stato della memoria. Osserva la quantità di RAM 
disponibile.  
Passo 1 — Stato memoria:  
free -m  
RISULTATO: memoria disponibile.  
 
Passo 2 — Stress memoria:  
stress --ram 1 --vm-bytes 1G  
RISULTATO: consumo RAM.  
Esegui stress --ram 1 --vm-bytes 1G per occupare memoria. Ripeti free -m e 
osserva la differenza.  
 
Passo 3 — Verifica:  
free -m  
RISULTATO: memoria libera diminuisce.  
INTERPRETAZIONE: memoria finita = sistema rallenta.  
Quando la memoria libera diminuisce, il sistema deve gestire le risorse in 
maniera più complessa. Se la memoria finisce, si verificano rallentamenti.  
 

5 
 
4. Analisi della Rete  
Passo 1 — ARP table:  
ip neigh  
RISULTATO: elenco IP e MAC noti. Esegui ip neigh per visualizzare la tabella 
ARP, che associa indirizzi IP a indirizzi MAC.  
 
Passo 2 — Pulizia:  
sudo ip neigh flush all  
RISULTATO: tabella vuota.  
Pulisci la tabella con sudo ip neigh flush all e verifica che sia vuota. La tabella 
resta vuota per pochi secondi, perche lamacchina subito contatta il 
gateway per verificare la connettivita: per vedere tabella arp vuota 
ocnviene dare insieme sudo … e ip neigh. 
 
Passo 3 — Ping esterno:  
ping 8.8.8.8  
RISULTATO: connessione Internet.  
Esegui ping 8.8.8.8 e poi ping verso un IP interno. Successivamente controlla 
nuovamente ip neigh.  
 
Passo 4 — Ping interno:  
ping 10.0.0.5  
RISULTATO: comunicazione rete privata.  
 
Passo 5 — Verifica ARP:  
ip neigh  
RISULTATO: nuove entry.  
INTERPRETAZIONE: ARP si popola solo dopo comunicazione.  
 
La tabella ARP si riempie nuovamente. Questo dimostra che il sistema 
apprende dinamicamente i dispositivi presenti sulla rete. Openstack e 
hypervisor lavorano a livello 2.  


---

# Virtualizzazione 26 - Infrastruttura virtuale

**File:** `Virtualizzazione 26 - Infrastruttura virtuale.pdf`
**Tipo:** `.pdf`
**Dimensione:** 1959.0 KB
**Ultima modifica:** 02/07/2026 09:25

---

Paolo BELLONI [paolo.belloni@its-ictpiemonte.it]DOCENTE
Sistemi di VirtualizzazioneUnità Formativa
Infrastruttura VirtualeArgomento


P . Belloni  | 
InfrastrutturaVirtuale
Componenti software (softwarizzate, astratte) che abilitano l’esecuzione di
applicazioni senza disporre di una macchina fisica
• Macchine Virtuali
• Container
• K8S
• Cloud Service Provider
2

P . Belloni  | 
I livelli di Virtualizzazione1/4
A che livello eseguire la virtualizzazione?
• Dipende dalle interfacce offerte dai vari
componenti del sistema.
▪ Interfaccia tra HW e SW (user ISA: istruzioni
macchina non privilegiate, invocabili da ogni
programma).
▪ Interfaccia tra HW e SW (system ISA: istruzioni
macchina invocabili solo da programmi
privilegiati).
▪ Chiamate di Sistema: Application Binary
Interface.
▪ Chiamate di libreria: Application Programming
Interface.
• Obiettivo della virtualizzazione
▪ Imitare il comportamento di queste interfacce
3
1
1
2
2
3
4
3 4

P . Belloni  | 
I livelli di Virtualizzazione2/4
Cinque livelli di virtualizzazione
• Livello ISA (Instruction Set Architecture).
▪ Si implementa emulando l’ISA, attraverso una traduzione di ogni singola istruzione oppure
attraverso dynamic binary translation (converte in blocchi piuttosto che istruzione per
istruzione).
• Livello Hardware (aka HW Abstraction Layer HAL oppure system VM) .
▪ Bastato su hypervisor.
• Livello Sistema Operativo (aka containers).
• Livello Run-time Library.
• Livello applicazione utente (aka process VM).
4

P . Belloni  | 
I livelli di Virtualizzazione3/4
5


P . Belloni  | 
I livelli di Virtualizzazione4/4
6


VM – Virtualizzazionea livello HW
7

P . Belloni  | 
La Virtualizzazionea livello HW (System Level VM)
• La virtualizzazione a livello HW o system level VM si ottiene attraverso un hypervisor.
Definizioni
• Un Hypervisor è un software di virtualizzazione che permette di eseguire diversi SO
contemporaneamente sulla stessa macchina fisica, interagendo direttamente con le
risorse fisiche del server. L’hypervisor ha due componenti:
▪ un Kernel – un SO per sistemi operativi;
▪ un Virtual Machine Monitor (VMM), che astrae l’HW per apparire come una
macchina fisica (con CPU, memoria e I/O propri). A volte VMM sinonimo di
hypervisor.
• Host – piattaforma base sulla quale sono eseguite le varie VM.
▪ Composta da macchina fisica, opzionalmente SO host, hypervisor.
• Guest – tutto quanto si trova all’interno di una VM.
▪ SO guest e applicazioni eseguite dentro la VM.
8

P . Belloni  | 
La Virtualiz. a livello HW e l’ Allocazionedelle Risorse
9


P . Belloni  | 
Classificazionedella Virtualizzazionea livello HW  
Esistono diversi tipi di virtualizzazione a livello HW (o system level virtualization),
distinti in base a:
❖Dove si istanza l’hypervisor:
▪ System hypervisor, o di sistema, chiamato anche type-1, native or bare-metal 
hypervisor;
▪ Hosted hypervisor, o ospitato, chiamato anche type-2 hypervisor.
❖Come si virtualizzano le istruzioni sensibili e non virtualizzabili.
▪ Full virtualization:
▪ Software-assisted;
▪ Hardware-assisted.
▪ Para-virtualization.
10

P . Belloni  | 
Classificazione della Virtualizzazione a livello HW 
11
Container

P . Belloni  | 
Hypervisor di Sistema vs Ospitato 1/2
In quale livello dell’architettura di sistema si colloca l’hypervisor?
➢Direttamente sull’hardware: hypervisor di sistema
➢Sopra il SO host: hypervisor ospitato
12
Hardware
Hypervisor
Hardware
Hypervisor
Host OS
Application
Guest OS-1
VM-1
Application
Guest OS-n
VM-n
Application
Guest OS-1
VM-1
Application
Guest OS-n
VM-n
Host Guest
Host Guest
Hypervisor di sistema Hypervisor ospitato

P . Belloni  | 
Hypervisor di Sistema vs Ospitato 2/2
• Hypervisor di sistema (type-1): eseguito direttamente sull’hw, offre funzionalità di
virtualizzazione integrate in un SO semplificato (è, di fatto, un SO).
▪ L’hypervisor può avere un’architettura a micro-kernel (solo funzioni di base, no
device driver) o monolitica.
▪ Richiede HW certificato.
▪ Esempi: Xen, KVM (non univocamente riconosciuto), VMware ESX, Hyper-V.
• Hypervisor ospitato (type-2): eseguito sul SO host, accede alle risorse hw tramite le
chiamate di sistema del SO host.
▪ Interagisce con il SO host tramite l’ ABIed emula l’ISA di hw virtuale per i SO guest.
▪ Vantaggio: può usare il SO host per gestire le periferiche ed utilizzare servizi di basso
livello (es. scheduling delle risorse).
▪ Vantaggio: non occorre modificare il SO guest.
▪ Svantaggio: degrado delle prestazioni rispetto a hypervisor di sistema
▪ Esempi: Bochs, Parallels Desktop, VirtualBox.
13

P . Belloni  | 
Virtualizzazione completa (full)
▪ L’hypervisor espone ad ogni VM interfacce hw
simulate funzionalmente identiche a quelle
della sottostante macchina fisica.
▪ L’hypervisor intercetta le richieste di accesso
privilegiato all’hw (ad es. istruzioni di I/O) e ne
emula il comportamento atteso.
▪ Esempi: KVM, VMware ESXi, Microsoft Hyper-
V.
Full-Virtualization vs Para-Virtualization
Quale modalità di dialogo tra la VM e hypervisor per l’accesso alle risorse fisiche,
ovvero come gestire l’esecuzione di istruzioni privilegiate?
➢Virtualizzazione completa
➢Paravirtualizzazione
14
Para-Virtualizzazione
▪ L’hypervisor espone ad ogni VM interfacce hw
simulate funzionalmente simili (ma non
identiche) a quelle della sottostante macchina
fisica.
▪ Non viene emulato l’hw, ma viene creato uno
strato minimale di sw (Virtual Hardware API)
per assicurare la gestione delle VM ed il loro
isolamento.
▪ Esempi: Xen, Oracle VM (basato su Xen),
PikeOS.

P . Belloni  | 
Riassumendo i diversi approcci di Virtualizzazione
15
Host Hardware (x86)
Ring 3
Ring 2
Ring 1
Ring 0
User Apps
Hypervisor
Guest OS
User Apps
Hypervisor
Para-virtualized
Guest OS
User Apps
Hypervisor
Guest OS
Hypercall
Binary Translation
OS Request Trap to VMM
Paravirtualization Full Virtualization HW-Assisted
Xen, KVM VMware ESX/ESXi, 
Microsoft Hyper-V 
Intel VT-x, AMD-V

P . Belloni  | 
L’operativitàdella Virtual Machine (VM)
• Dal punto di vista dell’utente, una VM è
un logical compute system (sistema
logico per il processamento dei dati).
▪ Lavora su un SO e ha applicazioni come
una macchina fisica.
▪ Dispone di componenti virtuali come
CPU, RAM, dischi e interface di rete.
▪ Dal punto di vista dell’hypervisor invece:
▪ Una VM è un insieme discreto di file (file
di configurazione, file di dischi virtuali,
file di virtual BIOS, file di VM swap e log
file).
16Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
SERVER
VM1 VM3VM2
Hypervisor
Driver
CPU
Driver Driver
NIC
Driver
DISKMemory
OS2 OS2
ApplicationApplication
OS1
Application

P . Belloni  | 
I file della Virtual Machine (VM) 1/2
17Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011


P . Belloni  | 
I file della Virtual Machine (VM) 2/2
18Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
DescriptionUsageFile
Virtual machine configuration filevmname.vmx.vmx
Additional virtual machine 
configuration files
vmname.vmxf.vmxf
Virtual disk characteristicsvmname.vmdk.vmdk
Virtual machine data diskvmname-flat.vmdk-flat.vmdk
Virtual machine BIOS or EFI 
configuration
vmname.nvram or nvram.nvram
Virtual machine paging backup filevmname.vmem.vmem
Virtual machine snapshots 
information (metadata) file
vmname.vmsd.vmsd
Virtual machine memory snapshot 
file
vmname.vmsn.vmsn
Virtual machine swap filevmname.vswp.vswp
Virtual machine suspend filevmname.vmss.vmss
Current virtual machine log filevmware.log.log
Old virtual machine log filesvmware-#.log (where # is a number 
starting with 1)
-#.log
Scoreboard files contain 
performance information about 
the VM
vmware-#.scoreboard (where # is a
number starting with 1)
.scoreboard
Location: storage/datastore1/vmname

P . Belloni  | 
I file system per la gestione dei file di VM
19Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
I file system (formati) supportati da hypervisor sono:
• Virtual Machine File System (VMFS).
▪ È un file aggregato che permette alle diverse macchine fisiche di
leggere/scrivere sullo stesso storage contemporaneamente.
▪ Può essere istanziato su storage esterno FC e iSCSI, oltre che su storage locale.
• Network File System (NFS).
▪ Abilita l’archiviazione dei file di VM su un file server remoto (Network
Attached Storage NAS).
▪ Il client NFS è implementato in hypervisor.

P . Belloni  | 
L’HW della Virtual Machine
20Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011


P . Belloni  | 
I componentiHW della Virtual Machine (VM)
21Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

Container – Virtualizzazionea 
livello SO
22

P . Belloni  | 
La Virtualizzazionea livello di SO 1/2
• Finora abbiamo considerato la virtualizzazione a livello hardware.
• Analizziamo ora la virtualizzazione a livello di sistema operativo (o container-
based virtualization).
• Permette di eseguire molteplici ambienti di esecuzione tra di loro isolati
all’interno di un singolo SO.
▪ Tali ambienti sono chiamati:
➢container;
➢jail;
➢zone;
➢virtual execution environment (VE).
23

P . Belloni  | 
La Virtualizzazionea livello di SO 2/2
24
Type 1
Virtualizzazione a livello SOVirtualizzazione a livello HW
Type 2
Heavy-weight Light-weight
Hardware
Container Engine
OS
Application
Container-1
Application
Container-n

P . Belloni  | 
La Virtualizzazionea livello di SO: Vantaggi
Rispetto alla virtualizzazione a livello HW.
• Minimo degrado delle prestazioni.
➢ Le applicazioni invocano direttamente le system call, senza mediazioni di hypervisor.
• Tempo di startup e shutdown minimi.
➢ Secondi per container, minuti per VM.
• Alta densità.
➢ Centinaia di istanze sulla singola macchina fisica (PM).
• Dimensione dell’immagine più piccola (footprint).
➢ Non include il kernel di SO.
• Possibilità di condividere le pagine di memoria tra i diversi container in esecuzione sulla
stessa PM.
• Portabilità e interoperabilità migliori.
• Le applicazioni su container sono indipendenti dall’ambiente di esecuzione.
25

P . Belloni  | 
La Virtualizzazionea livello di SO: Svantaggi
Rispetto alla virtualizzazione a livello HW.
• Minore flessibilità.
➢Non posso coesistere diversi SO sulla stessa PM.
• Solo applicazioni native per i SO supportati (p. es. solo applicazioni native per
Linux).
• Meno isolamento.
• Maggiore rischio di vulnerabilità.
• La singola vulnerabilità nel kernel di SO compromette l’intero sistema.
26

P . Belloni  | 
Confrontotra Virtualizzazionea livello HW vs SO
27


P . Belloni  | 
Metodologieper Virtualizzazionea livello di SO (1)
• Il kernel del SO consente l’esistenza di diverse istanze isolate di spazi d’utente, chiamate
container, che condividono però le risorse (di CPU, memoria e storage) di un SO host.
• Ogni container è costituito da:
➢ insieme di processi;
➢ file system;
➢ utenti;
➢ interface di rete con relativi indirizzi IP;
➢ tabelle di routing;
➢ regole di configurazione del firewall, … .
• I container condividono lo stesso SO, in particolare, il kernel di SO.
28


P . Belloni  | 
Solo Linux?
• Windows e OS X supportano la virtualizzazione basata su container.
➢Docker Desktop è una applicazione per Windows e Mac (o Linux) che
permette di installare un Docker Engine su Windows OS > 10 o MacOS.
• Alternative: installare una VM con Linux come guest OS e utilizzare la
virtualizzazione basata su SO all’interno della VM.
➢Ovviamente, impatto sulle prestazioni.
➢Le applicazioni containerizzate devono girare su Linux (non sono possibili
applicazioni native OS X o Windows).
29

P . Belloni  | 
I container abilitano nuove tecnologie
• In sintesi, l’uso dei container permette di avere l’applicazione e tutte le sue
dependencies (tutto il sw che serve per farla funzionare correttamente, in pratica
i file bins/libs – binary e le librerie) in un singolo “contenitore”, che permette
quindi di eseguirlo pressoché in ogni ambiente.
• I container risultano più efficienti rispetto alle VM, perché utilizzano meno
risorse.
Inoltre,
• I container sono la tecnologia chiave per abilitare i micro-servizi (microservice) e il
cloud serverless (serverless computing).
30

P . Belloni  | 
I Microservice
31


P . Belloni  | 
Container as a Service – CaaS
• Anche la tecnologia di virtualizzazione a livello di SO, basata su container, viene
usata dai provider per offrire i servizi del Cloud. Si parla in questo caso di
Container as a Service.
• Il servizio cloud di CaaS permette di sviluppare e gestire delle applicazioni usando
i container.
• Il CaaS si colloca tra IaaS e PaaS. Tuttavia sarebbe più appropriato classificarlo
come un sottocaso di IaaS, in cui la risorsa base è rappresentata dal container.
• Tecnologia ampiamente diffusa sul mercato:
➢Amazon Elastic Container Service (ECS);
➢Microsoft Azure Container;
➢Google Container Engine;
➢Alauda (CaaS solution);
➢Docker Cloud.
32

P . Belloni  | 
Container Orchestration
• Quando un’applicazione è costituita da più container (multi-container application),
distribuiti in cluster dinamici su larga scala, si rende necessario l’utilizzo di una
piattaforma funzionale che gestisca il ciclo di vita dei suoi container costituenti.
• Questa piattaforma prende il nome di Orchestrator.
• L’orchestrator permette di configurare, attivare/istanziare (deployment), monitorare e
controllare dinamicamente le applicazioni su container. Di fatto, integra e gestisce i
container allocando le risorse rese necessarie dalle richieste degli utenti.
• Alcuni esempi:
➢ Kubernetes (K8s);
➢ Docker Swarm;
➢ Amazon Elastic Container Service;
➢ Google Kubernetes Engine;
➢ Marathon;
➢ Nomad (container orchestrator per Mesos).
33
Servizi Cloud “fully-managed”

P . Belloni  | 
Il modello Google: tutto è su container
• Da anni Google ha cambiato il suo paradigma di gestione dei DC, da V-DC
machine-oriented a V-DC application-oriented.
• Questo application-oriented shift, come viene chiamato, è stato possibile grazie
alla trasformazione dei V-DC utilizzando la tecnologia dei container.
• “Goal: let container technology operate at Google scale.
▪ Everything at Google runs in containers.
▪ Google launches several billion containers per week into Google Cloud”.
• Fondamentale il ruolo di un orchestrator nell’ottenere tali strabilianti prestazioni.
▪ Borg and Omega, sono sistemi proprietari puramente interni a Google,
predecessori di Kubernetes.
▪ Kubernetes: piattaforma di container orchestration open-source.
34

P . Belloni  | 
Kubernetes (K8s)
• “Google’s Kubernetes, also known as K8s, is an open-source system for
automating deployment, scaling, and management of containerized applications”.
• http://kubernetes.io
• Principali caratteristiche:
➢Portable: public, private, hybrid, multi-cloud;
➢Extensible: modular, pluggable, hookable, composable;
➢Self-healing: auto-placement, auto-restart, auto-replication, auto-scaling of
containers.
• Funziona su piattaforme di cloud pubblico e privato (AWS, Microsoft Azure,
OpenStack, Apache Mesos) e anche su bare metal.
• Standard di fatto, offerto dalla maggioranza dei provider come servizio Cloud.
35
Source: http://kubernetes.io


P . Belloni  | 
Kubernetes (K8s): Pod
• Pod: the smallest deployable units of computing that you can create and manage in
Kubernetes.
• A Pod (as in a pod of whales or pea pod) is a group of one or more (tightly coupled)
containers, with shared storage and network resources, and a specification for how to
run the containers.
• A Pod's contents are always co-located and co-scheduled, and run in a shared context.
• The shared context of a Pod is a set of Linux namespaces, cgroups, and potentially other
facets of isolation - the same things that isolate a container. So a Pod is similar to a set of
containers with shared namespaces and shared filesystem volumes.
• Kubernetes gives pods their own IP addresses and a single DNS name for a set of pods, 
and can load-balance across them.
• Users organize pods using labels:
▪ Label: arbitrary key/value pair attached to pod;
▪ E.g., role=frontend and stage=production.
36Source: http://kubernetes.io


P . Belloni  | 
Kubernetes (K8s): architettura1/3
37Source: https://kubernetes.io/docs/concepts/overview/components/


P . Belloni  | 
Kubernetes (K8s): architettura2/3
38Source: https://kubernetes.io/docs/concepts/overview/components/


P . Belloni  | 
Kubernetes (K8s): architettura3/3
39
• L’architetturadi K8s è organizzata secondo un framework master-worker.


P . Belloni  | 
Un approccio innovativoallo sviluppo del sw 1/3
• I container forniscono una nuovo modo per costruire, impacchettare, condividere
e distribuire le applicazioni.
• In particolare, i container supportano l’introduzione di nuove metodologie per lo
sviluppo e la distribuzione del sw: CI/CD e DevOps e Agile.
40
• Continuous Integration and Continuous
Deployment CI/CD: questo paradigma
descrive le fasi chiave in un flusso
automatico di sviluppo e distribuzione del
sw. Questo flusso include design, coding,
testing, integrazione, delivery, validation e
deployment, prima della fase di operation
nell’ambiente finale.
• I container (più della VM) permettono agli
sviluppatori di creare codice in modo
collaborativo, condividendo facilmente le
immagini sw, mentre semplificano la
distribuzione verso le differenti
infrastrutture.


P . Belloni  | 
Un approccio innovativoallo sviluppo del sw 2/3
41
• Development and Operations
DevOps: Metodologia di sviluppo sw
creata per ridurre o eliminare il divario
tra sviluppo e operation, enfatizzando
comunicazione, collaborazione,
integrazione, quality assurance e
delivery con un deployment
automatico.
• Di fatto, la metodologia vuole
bilanciare l’aspirazione per veloci
cambiamenti del team di sviluppo con
il desiderio di stabilità del team di
operation, attraverso comunicazione e
collaborazione efficaci.


P . Belloni  | 
Un approccio innovativoallo sviluppo del sw 3/3
42
• DevOps è una pratica di sviluppo agile e una
mentalità che utilizza principi agili
(collaborazione, comunicazione, utilizzo degli
strumenti giusti) per semplificare la
costruzione, il test e il rilascio del software.
• CI/CD è una tattica DevOps, che utilizza i giusti
strumenti di test automatizzati per
implementare lo sviluppo agile.
• Agile è un ampio framework che comprende le
altre due pratiche. Si concentra sui processi
che evidenziano il cambiamento mentre
accelera la distrubuzione. È una filosofia di
sviluppo software che viene implementata in
varie metodologie: Scrum, Kanban, Scaled
Agile Framework (SAFe), ecc.
• Tutte e tre le pratiche hanno lo stesso
obiettivo: creare software migliore in minor
tempo. Queste pratiche si sovrappongono
quasi sempre.


IaC
43

P . Belloni  | 
Infrastructure as Code (IaC)
• Infrastructure as Code (IaC) è un approccio che permette di definire, creare e gestire
l’infrastruttura IT tramite codice, invece di configurazioni manuali.
• Concetti chiave:
✓ Infrastruttura descritta con file di testo
✓ Versionabile (Git)
✓ Automatizzabile e ripetibile (idempotenza)
✓ Specifico lo stato desiderato (IaC dichiarativa, la più recente [2010] vs IaC procedurale/imperativa)
• Quale infrastruttura?
➢ Container Docker
➢ Volumi e reti
➢ VM e cluster Kubernetes (anche su AWS o Azure)
• Esempio: creo VM, rete e storage scrivendo codice invece di usare una console cloud
44

P . Belloni  | 
Infrastructure as Code (IaC): Perchè?
• IaC risolve i limiti della gestione manuale
✓Coerenza tra ambienti (dev / test / prod)
✓Riproducibilità dell’infrastruttura
✓Riduzione degli errori umani
✓Velocità di creazione degli ambienti
• Il configuration drift è la situazione in cui lo stato reale
dell’infrastruttura non coincide più con lo stato definito nel
codice (IaC).
➢In pratica: il codice dice una cosa, l’infrastruttura reale ne fa un’altra
✓Qualcuno modifica a mano un server (SSH, console cloud)
✓Una configurazione cambia fuori dal codice
✓Script procedurali vengono eseguiti solo parzialmente
45

P . Belloni  | 
Infrastructure as Code (IaC)
Come si usa (flusso tipico)?
• Scrivo codice IaC
• Versiono su Git
• plan → anteprima
• apply → crea/modifica infrastruttura
46

P . Belloni  | 
Infrastructure as Code (IaC): dichiarativavs 
procedurale
1. Crea una VM
2. Installa Docker
3. Avvia il container
4. Crea directory
Descrive i passi da eseguire,
nell’ordine, per ottenere
l’infrastruttura desiderata
47
Voglio:
- 1 VM
- 1 container in esecuzione
- 1 volume persistente
Descrive lo stato finale
desiderato dell’infrastruttura,
senza specificare i passi per
arrivarci

P . Belloni  | 
Infrastructure as Code (IaC): Come si implementa?
• File di definizione (codice)
• Motore che applica lo stato desiderato
Dipendenze tecnologiche: IaC non vive da sola, dipende da:
➢Virtualizzazione (VM, hypervisor)
➢Container (Docker, Kubernetes)
➢Cloud (pubblico, privato, ibrido)
➢API dell’infrastruttura
• IaC non è solo cloud: vale anche per data center on-prem
• Use case: Creare ambienti test e produzione identici
48

P . Belloni  | 
Infrastructure as Code (IaC): Architettura
[ File IaC ]     
↓
[ Motore IaC ]     
↓
[ Provider / Driver ]
↓
[ Infrastruttura reale ]
49

P . Belloni  | 
Infrastructure as Code (IaC): Come si implementa?
• Il motore è il componente che interpreta il codice IaC e lo
trasforma in azioni reali sull’infrastruttura, chiamando le API del
cloud o della piattaforma sottostante
• Cosa fa concretamente un motore IaC?
➢Legge il codice/template (YAML, JSON, HCL, Bicep, ecc.)
➢Valida che sia corretto
➢Calcola lo stato desiderato
➢Confronta lo stato desiderato con quello reale
➢Decide le operazioni da eseguire (create / update / delete)
➢Chiama le API dell’infrastruttura
➢Tiene traccia dello stato (implicitamente o esplicitamente)
50

P . Belloni  | 
Infrastructure as Code (IaC): Linguaggi e Strumenti
51
Uso tipicoTipoOpen SourceProduttoreLinguaggioStrumento
Multi-cloudDichiarativoParzialeHashiCorpHCLTerraform
Fork di 
Terraform per 
restare open-
source
DichiarativoSìLinux 
FoundationHCLOpenTofu
Configurazione
OS/appProceduraleSìRed HatYAMLAnsible
Solo AWSDichiarativoNoAWSYAML/JSONCloudFormation
Solo AzureDichiarativoSi Microsoft AzureBicep/ARM JSONARM

P . Belloni  | 
Infrastructure as Code (IaC): Vantaggi
• Source of Truth: il codice è la verità ufficiale
• Ambienti coerenti e ripetibili
• Automazione e velocità
• Base del DevOps
• Integrazione con GitHub
✓Codice IaC in repository Git
✓Pull Request = modifica infrastruttura
✓CI/CD → deploy automatico dell’infra
❑ATT: errore di codice = errore di infra!
52

P . Belloni  | 
Infrastructure as Code (IaC):
alcuni provider ufficiali Terraform
terraform {
required_providers {
aws = {
source = "hashicorp/aws"
version = "~> 5.0"
}
}
}
53

P . Belloni  | 
Infrastructure as Code (IaC):
alcuni provider ufficiali Terraform
terraform {
required_providers {
aws = {
source = "hashicorp/aws"
version = "~> 6.0"
}
}
}
provider "aws" {
region = "eu-west-1" # esempio: Irlanda
}
############################################
# 2. Region corrente (lettura dinamica)
############################################
data "aws_region" "current" {}
54

P . Belloni  | 
Infrastructure as Code (IaC):
alcuni provider ufficiali Terraform
############################################
# 3. Availability Zones
# Le AZ sono unità di isolamento fisico
# Concettualmente ≃ datacenter
############################################
data "aws_availability_zones" "available" {
state = "available"
}
############################################
# 4. VPC esistente
# In AWS la VPC è il perimetro di rete principale
############################################
data "aws_vpc" "selected" {
tags = {
Name = "main-vpc"
}
}
55

P . Belloni  | 
Infrastructure as Code (IaC):
alcuni provider ufficiali Terraform
############################################
# 5. Subnet esistente
# Le subnet sono sempre:
# - dentro una VPC
# - associate a UNA sola AZ
############################################
data "aws_subnet" "public_a" {
vpc_id = data.aws_vpc.selected.id
availability_zone = data.aws_availability_zones.available.names[0]
tags = {
Name = "public-a"
}
}
56

P . Belloni  | 
Infrastructure as Code (IaC):
alcuni provider ufficiali Terraform
############################################
# 6. Security Group
# Firewall STATEFUL
# Associato a ENI / EC2 / LB
############################################
data "aws_security_group" "web_sg" {
name = "web-sg"
vpc_id = data.aws_vpc.selected.id
}
############################################
# 7. Network ACL (NACL)
# Firewall STATELESS
# Associato alle subnet
############################################
data "aws_network_acl" "main" {
vpc_id = data.aws_vpc.selected.id
tags = {
Name = "main-nacl"
}
}
57

P . Belloni  | 
Infrastructure as Code (IaC):
alcuni provider ufficiali Terraform
terraform {
required_providers {
azurerm = {
source = "hashicorp/azurerm"
version = "~> 3.0"
}
}
}
58

P . Belloni  | 
Infrastructure as Code (IaC):
alcuni provider ufficiali Terraform
terraform {
required_providers {
google = {
source = "hashicorp/google"
version = "~> 5.0"
}
}
}
59

P . Belloni  | 
Infrastructure as Code (IaC):
alcuni provider ufficiali Terraform
terraform {
required_providers {
kubernetes = {
source = "hashicorp/kubernetes"
version = "~> 2.0"
}
}
}
60

P . Belloni  | 
Infrastructure as Code (IaC):
alcuni provider ufficiali Terraform
terraform {
required_providers {
vsphere = {
source = "hashicorp/vsphere"
version = "~> 2.0"
}
}
}
61


---

# Virtualizzazione 26 - La Virtualizzazione di Mem

**File:** `Virtualizzazione 26 - La Virtualizzazione di Mem.pdf`
**Tipo:** `.pdf`
**Dimensione:** 709.0 KB
**Ultima modifica:** 02/07/2026 09:25

---

DOCENTE Paolo BELLONI [paolo.belloni@its-ictpiemonte.it]
Unità Formativa Elementi di Virtualizzazione
Argomento La virtualizzazione della memoria
1

Elementi di Virtualizzazione | 
Richiami sulla memoria 1/4
2
• La memoria principale può agire come “cache” per la memoria di massa (dischi,
nastri).
• Si parla in questo caso di memoria virtuale:
▪ I programmi sono compilati rispetto ad uno spazio di indirizzamento virtuale, diverso 
da quello fisico;
▪ Il sistema di memoria virtuale traduce gli indirizzi virtuali in indirizzi fisici.
• Vantaggi:
▪ illusione di avere una maggiore memoria fisica;
▪ meccanismi di protezione (gli spazi virtuali di programmi diversi mappati su spazi
fisici differrenti).
2

Elementi di Virtualizzazione | 
Richiami sulla memoria 2/4
3
• La memoria e organizzata in modo 
gerarchico (a livelli):
• Liv. 1: memoria più veloce(costosa).
• Liv. N: memoria più lenta (economica).
• Il processore indirizza tutta la memoria 
di Liv. N, ma accede direttamente solo 
al Liv. 1.
• La pagine cercate si trovano al livello 1
con maggiore probabilità.
Liv. 1
Livello 2
…
Livello N
CPU
3

Elementi di Virtualizzazione | 
Richiami sulla memoria 3/4
4
• Ad ogni istante solo una parte delle pagine di memoria “virtuale” è presente nella
memoria fisica.
• Quando la pagina cercata non è in memoria e deve essere letta da disco, si parla di page
fault (miss).
• Il costo dei page fault è estremamente elevato (milioni di cicli), e questo influenza molte 
scelte (dimensioni della pagina 4, 16, 32, 64 KB, gestione software).
• L’indirizzo virtuale si suddivide in Virtual Page Address  + offset.
• Il Virtual Page Address indirizza le entry di una tabella, detta Page Table, che contiene 
informazioni sulla presenza / validità delle pagine in memoria.
• In un sistema di memoria virtuale, ogni accesso alla memoria richiede due accessi: prima 
alla Page Table e quindi alla memoria fisica.
• Per ridurre questo overhead si sfrutta un meccanismo detto TLB (Translation Lookaside 
Buffer), una sorta di cache della Page Table. La TLB contiene copia delle entry della Page 
Table riferite recentemente, e, come la cache, può sfruttare l’associatività per ridurre i 
conflitti. 
4

Elementi di Virtualizzazione | 
Richiami sulla memoria 4/4
5
5

Elementi di Virtualizzazione | 
La virtualizzazionedella memoria 1/2
6
• In un ambiente non-virtualizzato:
▪ Utilizzando le page table, si passa dalla memoria virtuale alla memoria fisica.
▪ Si parla di one-level mapping.
• In un ambiente virtualizzato:
▪ Tutte le VM condividono la stessa memoria fisica e hypervisor deve ripartirla tra le
VM.
▪ Si parla di two-level mapping: dalla memoria virtuale guest alla memoria fisica guest
alla memoria fisica host.
• Terminologia:
➢Guest virtual memory: memoria visibile alle applicazioni; spazio di indirizzamento 
virtuale continuo presentato dal guest OS alle applicazioni.
➢Guest physical memory: memoria visibile al guest OS.
➢Host physical memory: memoria hw reale visibile ad hypervisor.
6

Elementi di Virtualizzazione | 
La virtualizzazionedella memoria 2/2
7
• Two-level memory mapping:
• Per passare dalla guest virtual memory alla host physical memory serve un mapping
a due livelli:
Guest VA (virtual address) → guest PA (physical address) → host MA (machine
address)
• Guest physical address ≠ host machine address.
7

Elementi di Virtualizzazione | 
Shadow Page-Table SPT 1/2
8
• Per evitare la riduzione delle prestazioni derivanti da extra memory mapping,
l’hypervisor utilizza delle shadow page-table (SPT) al fine di accelerare il mapping.
▪ Mapping diretto guest virtual su host physical memory address.
• SPT mappa direttamente l’indirizzo della guest virtual
memory nell’indirizzo della host physical memory.
▪ Il guest OS conserva la sua PT per memoria virtuale nello
spazio di guest physical memory assegnato.
▪ Per ogni dato in guest physical memory, l’hypervisor
dovrebbe mapparne l’indirizzo nel dato corrispondente
di host physical memory.
▪ SPT mappa direttamente l’indirizzo della guest virtual
memory nell’indirizzo della host physical memory.
▪ L’hypervisor deve mantenere aggiornata la SPT ad ogni
cambio che il guest OS attua sulle sue PT.
8

Elementi di Virtualizzazione | 
Shadow Page-Table SPT 2/2
9
• L’hypervisor utilizza l’hw di Translation Lookaside Buffer (TLB) per eseguire il
mapping diretto della memoria virtuale nella memoria di macchina fisica,
evitando il two-level mapping.
• Quando il guest OS cambia il mapping di guest virtual memory su guest physical 
memory, l’hypervisor aggiorna le sue SPT per mantenere un mapping diretto 
aggiornato.
9

Elementi di Virtualizzazione | 
Virtualizzazionedella memoria con SPT: Impatti
10
• Traduzione degli indirizzi.
▪ Il guest OS si aspetta indirizzi contigui, mentre la 
memoria fisica sottostante può apparire discontinua: 
hypervisor deve preservare questa illusione di 
continuità.
• Page table shadowing.
▪ L’implementazione di SPT è complessa.
▪ L’hypervisor intercetta le operazioni di paging e 
costruisce copia delle PT.
• Overhead.
▪ Ogni uscita dalla VM incrementa il tempo di 
esecuzione.
▪ SPT consuma una parte significativa della memoria di 
host.
▪ SPT deve essere sempre sincronizzato con le PT di 
guest.  
VM0 VMN
10

Elementi di Virtualizzazione | 
Virtualizzazionedella memoria con supporto HW
11
• SPT è una soluzione basata su sw. Esistono tuttavia 
soluzioni più efficienti, supportate da funzionalità specifiche 
hw.
▪ Second Level Address Translation (SLAT) è una
soluzione hardware-assisted per la virtualizzazione
della memoria, che traduce guest virtual address in 
host physical address.
▪ Dal 2006, Intel e AMD hanno introdotto nel loro hw il 
supporto della virtualizzazione di x86 (tecnologia Intel-
VTx* e AMD-V**, rispettivamente) includendo la 
funzione di SLAT con il nome di Extended Page Table 
(EPT) e Rapid Virtualization Indexing (RVI), 
rispettivamente.
▪ Con SLAT le prestazioni aumentano in modo 
significativo: misurato un guadagno del 42% rispetto al 
caso di SPT.
* Intel-VTx = Intel Virtualization Technology, precedentemente denominato Vanderpool (Pentium 4 mod. 662 e 672).
** AMD-V = AMD Virtualization.
VM0 VMN
The shadow page table code implementation can be critical from an overall 
performance point of view. To mitigate some of the page table shadowing related 
overheads, the concept of Extended page tables (EPT) was introduced in Intel 
Architecture based processors with Intel Virtualization technology enabled. EPT is 
optionally enabled in Xen when the guest is launched, when EPT is active the EPT 
based pointer loaded from the VMCS (VM Control Structure) data structure (part of 
Intel VT-x technology) points to extended page tables. This mechanism allows the 
Guest OSs full control of the Intel 64/IA-32 page tables which map guest-linear to 
guest-physical addresses. The new EPT page tables under VMM control and 
referenced by the EPT base pointer map guest-physical to host-physical addresses to 
access the memory allocated to the guest domains. This HW based mechanism 
prevents VM exits due to page faults, INVLPG (invalidate TLB entries), or CR3 accesses 
resulting in reduced paging related overheads.
CR3 = Control Register 3, used when virtual addressing is enabled, hence when the 
Paging PG bit is set in CR0. CR3 enables the processor to translate linear addresses 
into physical addresses by locating the page directory andpage tables for the current 
task.
11

Hardware-Assisted Memory Virtualization
Some CPUs, such as AMD SVM-V and the Intel Xeon 5500 series, provide hardware 
support for memory virtualization by using two layers of page tables.
The first layer of page tables stores guest virtual-to-physical translations, while the 
second layer of page tables stores guest physical-to-machine translation. The TLB 
(translation look-aside buffer) is a cache of translations maintained by the processor's 
memory management unit (MMU) hardware. A TLB miss is a miss in this cache and 
the hardware needs to go to memory (possibly many times) to find the required 
translation. For a TLB miss to a certain guest virtual address, the hardware looks at 
both page tables to translate guest virtual address to machine address. The first layer 
of page tables is maintained by the guest operating system. The VMM only maintains 
the second layer of page tables.
Performance Considerations
When you use hardware assistance, you eliminate the overhead for software memory 
virtualization. In particular, hardware assistance eliminates the overhead required to 
keep shadow page tables in synchronization with guest page tables. However, the TLB 
miss latency when using hardware assistance is significantly higher. By default the 
hypervisor uses large pages in hardware assisted modes to reduce the cost of TLB 
misses. As a result, whether or not a workload benefits by using hardware assistance 
primarily depends on the overhead the memory virtualization causes when using 
software memory virtualization. If a workload involves a small amount of page table 
activity (such as process creation, mapping the memory, or context switches), 
software virtualization does not cause significant overhead. Conversely, workloads 
with a large amount of page table activity are likely to benefit from hardware 
assistance.
By default the hypervisor uses large pages in hardware assisted modes to reduce the 
cost of TLB misses. The best performance is achieved by using large pages in both 
guest virtual to guest physical and guest physical to machine address translations.
The option LPage.LPageAlwaysTryForNPTcan change the policy for using large pages 
in guest physical to machine address translations.​
11

Elementi di Virtualizzazione | 
L’ottimizzazionedelle risorse di memoria
12Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
• L’hypervisor gestisce la memoria fisica di una macchina.
▪ Parte di questa memoria fisica è occupata direttamente dall’hypervisor.
▪ La restante parte di memoria resta disponibile per le varie VM.
• Le VM possono essere configurate per avere più memoria di quanta sia
fisicamente disponibile, con un meccanismo chiamato “memory over-
commitment”.
❖Di fatto, l’ottimizzazione della memoria viene attuato per permettere il memory over-
commitment.
• Le tecniche per gestire la memoria sono:
➢Transparent Page Sharing (TPS);
➢Memory Ballooning;
➢Memory Swapping.
The hypervisor manages the physical memory of compute systems. 
A part of memory is consumed by the hypervisor and rest of the memory is available 
for virtual machines (VMs).
Hypervisor allows configuring more memory to the virtual machines than what is 
physically available. This is known as overcommitment of memory. Memory 
overcommitment is allowed because, typically, some virtual machines are lightly 
loaded, compared to others. Their memory may be used infrequently, and much of 
the time, their memory remains idle. Memory overcommitment allows the 
hypervisor to use memory reclamation techniques to take the inactive or unused 
memory away from the idle virtual machines and give it to other virtual machines 
that will actively use it.
For example, consider a physical machine with 4GB physical memory running three 
virtual machines with 2GB VM memory each. Without memory overcommitment, 
only one virtual machine can be run because the hypervisor cannot reserve the 
physical memory for more than one virtual machine. This is because a hypervisor will 
consume some memory space and each virtual machine has a memory overhead.
In order to effectively support memory overcommitment, the hypervisor must 
provide efficient physical memory reclamation techniques. A hypervisor supports 
three techniques to reclaim memory: 
12

• transparent page sharing, 
• ballooning, and 
• memory swapping.
12

Elementi di Virtualizzazione | 
Memory Overhead di Hypervisor
13
• Hypervisor stesso impone un overhead nel consumo di 
memoria RAM.
• Overhead: consumo addizionale di risorse del 
"programma" hypervisor.
• In passato, l’hypervisor poteva occupare una parte 
significativa della memoria fisica, in alcuni casi fino al 20%.
• La tecnologia hypervisor più recente ha ridotto 
drasticamente tale quantità. 
➢ Per ogni VM viene riservata una piccola porzione di 
memoria addizionale + memoria allocata per 
l'utilizzo della macchina virtuale.
➢ Memoria addizionale utilizzata per funzioni 
operative (tabelle di mappatura della memoria, 
etc).
• L’overhead effettivo varia in base all'implementazione 
dell'hypervisor e alle configurazioni di memoria delle 
singole macchine virtuali.
• Esempio.
➢ Le due VM: 6 GB totali
➢ Hypervisor: 1 GB
➢ Memoria di riserva: 1 GB. Consente di 
fronteggiare picchi di carico transitori senza 
degradare le prestazioni.
13

Elementi di Virtualizzazione | 
Transparent Page Sharing (TPS)
14Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
• L’hypervisor identifica le pagine di memoria identiche tra le varie VM (p. es. stesso SO e stessa
applicazione su diverse VM) e le mappa sulla stessa pagina fisica, rimuovendo diverse copie della stessa
informazione (operazione trasparente alla VM, da cui il nome della tecnica).
▪ Utilizza una funzione di hash per confrontare le pagine di memoria e verificarne la similitudine.
▪ Quando la pagina fisica è condivisa, diventa read-only.
• Per la scrittura, l’hypervisor tratta le pagine condivise come “copy-on-write”.
• Cosa accade in caso di tentativo di scrittura su pagina condivisa da parte della legittima VM?
▪ Si genera un fault page non critico (minor fault page);
▪ Viene create un copia privata della pagina di memoria dopo la scrittura e su questa viene rimappata la
memoria della VM.
When multiple virtual machines (VMs) are running, some of them may have identical 
sets of memory content. This presents opportunities to share memory across virtual 
machines (as well as to share within a single virtual machine). For example, several 
virtual machines may run the same guest operating system, have the same 
applications, or contain the same user data. With page sharing, the hypervisor can 
reclaim the redundant copies and keep only one copy, which is shared by multiple 
virtual machines in the physical memory. As a result, the total amount of physical 
memory consumed by virtual machines is reduced and memory overcommitment 
becomes possible.
A hypervisor identifies redundant page copies by their contents. This means that 
pages with identical content can be shared regardless of when, where, and how those 
contents are generated.
The hypervisor scans the content of VM memory for sharing opportunities.
After the candidate virtual machine page content is confirmed to match the content 
of an existing physical page, the virtual machine memory pointer is updated to point 
to the shared location, and the redundant physical memory copy is reclaimed. This 
mapping process is invisible to the virtual machine. 
When a write occurs on the shared page, the standard Copy-on-Write (CoW) 
14

technique is used to handle these writes. Any attempt to write to the shared pages 
will generate a minor page fault.
After a page fault occurs, the hypervisor will transparently create a private copy of 
the page for that virtual machine. It remaps the pointer to this private copy of the 
virtual machines. In this way, virtual machines can safely modify the shared pages 
without disrupting other virtual machines sharing that memory.
Transparent Page Sharing basics
In ESX, a 4KB page backing any guest page with content identical to another 4KB 
guest page can be shared regardless of when, where, and how those contents are 
generated. ESX periodically scans the content of guest physical memory for sharing 
opportunities. For each candidate page, a hash value is computed based on its 
content. The hash value is then used as a key to look up a global hash table, in which 
each entry records a hash value and the physical page number of a shared page. If the 
hash value matches an existing entry, a full bit-by-bit comparison of the page 
contents between the candidate page and the shared page is performed to exclude a 
false match. After a successful content match, the guest-physical to host-physical 
mapping of the candidate page is changed to the shared host-physical page, and the 
redundant host memory copy is reclaimed.
Transparent Page Sharing with large pages
In hardware-assisted memory virtualization systems, ESX will preferentially back guest 
physical pages with large host physical pages (2MB contiguous memory region 
instead of 4KB for regular pages) for better performance. If there is not a sufficient 
2MB contiguous memory region in the host (for example, due to memory 
overcommitment or fragmentation), ESX will still back guest memory using small 
pages (4KB). ESX will not share large physical pages because:
The probability of finding two large pages that are identical is very low.
The overhead of performing a bit-by-bit comparison for a 2MB page is much higher 
than for a 4KB page.
However, ESX still generates hashes for the 4KB pages within each large page during 
page scanning.
In the cases where host memory is overcommitted, ESX may have to swap out pages. 
Since ESX will not swap out large pages, during host swapping, a large page will be 
broken into small pages. ESX tries to share those small pages using the pre-generated 
hashes before they are swapped out. The motivation of doing this is that the 
overhead of breaking a shared page is much smaller than the overhead of swapping 
in a page if the page is accessed again in the future.
14

Conclusion
Given the above implementation, one may see zero or very little page sharing in 
hardware MMU systems when host memory is under committed. Page sharing occurs 
only when the host starts to swap out pages due to very high memory pressure. Note 
that with the above features, the ability to reclaim memory through page sharing in 
ESX is not degraded because ESX defers sharing pages until host free memory is very 
low.
14

Elementi di Virtualizzazione | 
Memory Ballooning
15Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
• Basata sul principio per cui, se una VM deve
rilasciare memoria, la scelta migliore è lasciare
che il guest OS identifichi il blocco da liberare,
conoscendo quale sia il meno recente.
• Il balloon (palloncino) altro non e’ che un driver
relativo ad una periferica inesistente (pseudo-
device driver) installato nel guest OS.
• Il balloon comunica con l’hypervisor, che lo
“gonfia” quando la VM deve rilasciare memoria:
il balloon richiede un aumento di spazio di
memoria al guest OS, che gliele assegna
rilasciando pagine di memoria tipicamente
meno recenti, in base a propri algoritmi interni
usuali.
• L’hypervisor assegna questa memoria rilasciata
ad un’altraVM, che ne ha bisogno.
• Quando non c’è esigenza di liberare memoria, il
palloncino è sgonfio.
• Il guest OS non è al corrente della
comunicazione tra balloon e hypervisor e non
conosce lo scopo del pseudo-driver.
Vmmemctl.sys driver in Guest OS
sched.mem.maxmemctl paramenter in VM options
Ballooning is a completely different memory reclamation technique, compared to 
page sharing.
When a virtual machine (VM) must yield memory, the best thing is to let the guest 
operating system of the VM select the memory pages to give up. The virtual machine 
knows which pages have been least recently used and can be freed up. Ballooning 
technique makes the guest operating system free some of the virtual machine 
memory.
The balloon driver is installed in the guest operating system as a pseudo-device driver 
and communicates with the hypervisor. The guest operating system is aware of the 
fact that the balloon driver is installed but not aware of its purpose. The driver’s 
function is to demand memory from the guest operating system and later to 
relinquish it under the control of the hypervisor. The guest operating system is not 
aware of the communication taking place between the balloon driver and
the hypervisor.
When a compute is not under memory pressure, no virtual machine’s balloon is 
inflated. But when memory becomes scarce, the hypervisor chooses a virtual 
machine and inflates its balloon. It instructs the balloon driver in the virtual machine 
to demand memory from the guest operating system. The guest operating system 
15

complies by yielding memory, according to its own algorithms.
The hypervisor can assign the relinquished pages to other virtual machines that 
require more memory.
The hypervisor can safely reclaim this physical memory because neither the balloon 
driver nor the guest operating system relies on the contents of these pages. This 
means that no processes in the virtual machine will intentionally access those pages 
to read or write. If any of these pages are reaccessed by the virtual machine for some 
reason, the hypervisor will treat it as normal virtual machine memory allocation and 
allocate a new physical page for that virtual machine.
15

Elementi di Virtualizzazione | 
Memory Swapping
16Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
• Ogni VM attiva ha bisogno del suo swap file.
▪ Lo swap viene utilizzato per liberare memoria RAM: il sistema operativo salva 
sul disco una porzione della memoria allocata, che quindi può essere liberata e 
riallocata per i programmi che ne hanno bisogno. Questa porzione contiene i dati che 
hanno minore probabilità di essere richiesti nel futuro, e in genere sono quelli meno 
recentemente utilizzati.
▪ Lo swap file viene creato quando la VM si attiva e cancellato quando la VM si spegne.
• Lo swap file ha dimensione uguale alla differenza tra il limite di memoria e la
memoria riservata alla VM (SWAPvmx = LIMITvmx – RESERVATIONvmx).
• L’hypervisor swappa la memoria della VM nel caso in cui la memoria sia scarsa.
• Lo swap di memoria rappresenza l’ultima opzione per gestire l’overcommitment
di memoria (dopo page sharing e ballooning), perchè ha un notevole impatto
sulle performance.
As a last effort to manage excessively overcommitted physical memory, the 
hypervisor will swap the virtual machine’s (VM’s) memory content to their swap files. 
When virtual machines are powered on, the hypervisor creates and assigns one swap 
file to each virtual machine. This swap file stores the virtual machine’s memory 
contents. If a physical machine cannot get enough memory through page sharing and 
memory ballooning, the hypervisor forcibly reclaims memory
from virtual machines by memory swapping. The hypervisor copies the VM page 
contents to their corresponding swap files before assigning the pages to the virtual 
machines that need memory.
The swap file size is determined by the difference between the virtual machine’s 
configured memory (or its memory limit) and its reservation.
Whenever a swap file is actively used, performance is severely penalized. When the 
virtual machine is powered off, the swap file of that virtual machine is deleted. When 
the virtual machine is powered back on, the swap file for that virtual machine is re-
created.
16


---

# Virtualizzazione 26 - La Virtualizzazione di Networking

**File:** `Virtualizzazione 26 - La Virtualizzazione di Networking.pdf`
**Tipo:** `.pdf`
**Dimensione:** 1607.0 KB
**Ultima modifica:** 02/07/2026 09:25

---

Paolo BELLONI [paolo.belloni@its-ictpiemonte.it]DOCENTE
Elementi di VirtualizzazioneUnità Formativa
La Virtualizzazione della Rete (Networking)Argomento

P . Belloni  | 
Il Modello ISO OSI
2


P . Belloni  | 
La Virtualizzazionedelle Rete 1/4
3Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
È il processo di segmentazione logica o raggruppamento di reti fisiche che porta alla
creazione di entità logiche single o multiple ma indipendenti, chiamate reti virtuali.
➢Una rete virtuale appare come una rete fisica ai nodi a questa connessi.
➢Il processo di virtualizzazione delle reti abilita la condivisione delle risorse di rete.
➢La virtualizzazione abilita il raggruppamento funzionale di nodi con gli stessi requisiti in
una unica rete virtuale, indipendentemente dalla loro localizzazione geografica.
➢Permette la comunicazione diretta tra nodi appartenenti alla stessa rete virtuale, senza
necessità di instradare i pacchetti, anche se attestati a reti fisiche diverse.
➢Viceversa, l’instradamento del traffico è necessario quando comunicano due nodi
appartenenti a due reti virtuali diverse, anche se attestati alla stessa rete fisica.
➢Segrega il traffico di gestione (incluso il network broadcast) all’interno della singola rete
virtuale, evitando che si propaghi in altre reti.
Network Virtualization

P . Belloni  | 
Rete Fisica
• Composta da:
▪ adattatori di rete;
▪ switch;
▪ router;
▪ bridge;
▪ ripetitori e hub.
• Fornisce connettività tra:
▪ server fisici che ospitano hypervisor;
▪ server fisici e client;
▪ server fisici e sistemi di storage.
La Virtualizzazionedelle Rete 2/4
4Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011


P . Belloni  | 
Rete di VM
• Si trova all’interno dei serve fisici.
• È composta da switch logici chiamati
switch virtuali, con funzione simile
agli switch fisici.
• Fornisce connettività tra VM
all’interno di un server fisico.
• Fornisce connettività al kernel
dell’hypervisor.
• Connette alla rete fisica.
La Virtualizzazionedelle Rete 3/4
5Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

P . Belloni  | 
• La rete di VM e la rete fisica sono virtualizzate per creare delle reti virtuali (p. es. Virtual Local
Area Network VLAN o Virtual Storage Area Network VSAN)
La Virtualizzazionedelle Rete 4/4
6Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011


P . Belloni  | 
Virtual Networking della VM 1/4
7


P . Belloni  | 
Virtual Networking della VM 2/4
8
• Creare sottoreti virtuali mediante switch di rete virtuali interni ed
esterni.
• Una rete virtuale è una rete privata definita dal software in un
ambiente virtuale.
• Uno switch di rete virtuale esterno consente di instradare il traffico
verso la rete esterna.
• Uno switch di rete virtuale interno non gestisce il traffico verso la
rete esterna. Viene usato per la costituzione di sottoreti virtuali.
• VM1: due NIC virtuali VNIC1 e VNIC2, ognuna connessa ad uno switch
virtuale e quindi a ciascuna delle reti virtuali.
• Le richieste che provengono da VNIC3 verranno trasmesse alla rete
fisica e al mondo esterno. Le risposte a tale richiesta seguono il
percorso al contrario, attraverso la NIC fisica, attraverso lo switch
virtuale esterno e di nuovo alla NIC virtuale della VM.
• Le richieste da VNIC2 saranno inoltrare allo switch virtuale interno per
la comunicazione con altre macchine virtuali.
• La VM3 può effettuare richieste solo tramite lo switch virtuale interno.
Questa è una strategia comune in un ambiente virtuale per proteggere
applicazioni e server da attacchi indesiderati:
• senza una connessione a una scheda di rete fisica, la VM3 non può
essere vista, tanto meno attaccata, da una fonte esterna.
• VM1 funge da firewall e, con pratiche di sicurezza appropriate,
protegge i dati contenuti nell'altra VM.

P . Belloni  | 
Virtual Networking della VM 3/4
9
• Rispetto alla slide precedente, aggiunto un
ulteriore switch virtuale per separare due
reti.
• Possono essere diverse organizzazioni
aziendali che richiedono spazi di rete
separati in cui lavorare (es: la produzione è
separata dal test e dallo sviluppo).
• Questa architettura migliora inoltre le
prestazioni riducendo il traffico su ogni
segmento e migliora la sicurezza limitando
l'accesso a ciascuna area.
• Una terza macchina virtuale viene aggiunta
all'host e può comunicare solo con il nuovo
switch virtuale esterno.


P . Belloni  | 
Virtual Networking della VM 4/4
10
• Nel caso il traffico dati dello storage viaggi
su una rete, è necessario allocare una
larghezza di banda adeguata per evitare
problemi di prestazioni.
• Ad esempio dedicando schede di rete
fisiche per il traffico dello storage, come
mostrato in figura.


P . Belloni  | 
Le Metodologieper la Virtualizzazionedella Rete
11Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
1. Basata sul SO dello switch fisico.
• Il SO deve avere una specifica funzionalità per la virtualizzazione della rete.
2. Basata sull’hypervisor.
▪ Una opzione è che l’hypervisor disponga di funzionalità integrate di networking e
virtualizzazione della rete.
❖Per creare switch virtuali e per configurare su quelli delle reti virtuali.
▪ In alternativa, l’hypevisor utilizza software di una terza parte, al fine di fornire
funzionalità di networking e virtualizzazione della rete.
❖Il software della terza parte viene installato sopra l’hypervisor.
❖Questo software rimpiazza le funzionalità di networking native dell’hypervisor.

P . Belloni  | 
I Benefici della Virtualizzazionedi Rete
12Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011


P . Belloni  | 
Infrastrutturadi rete in un VDC
13Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
• L’infrastruttura di rete di un Virtual Data Center (VDC) include componenti di rete sia fisica che
virtuale. Questi componenti sono connessi gli uni agli altri, per abilitare il flusso di traffico di
rete.

P . Belloni  | 
Connessione di Rete e Flusso di Traffico: Esempio 1
14Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011


P . Belloni  | 
Connessione di Rete e Flusso di Traffico: Esempio 2
15Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

P . Belloni  | 
Connessione di Rete e Flusso di Traffico: Esempio 3
16Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

P . Belloni  | 
I componentidella Rete Virtuale: Virtual NIC 
17Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
• Collega le VM al virtual switch.
▪ Il guest OS invia il traffico di I/O al VNIC utilizzando un driver, esattamente
come avviene per un NIC fisico.
• Il VNIC invia il traffico di I/O, in forma di pacchetti Ethernet, al virtual switch.
• Ha un unico MAC address e IP address. L’hypervisor genera il MAC address del
VNIC al momento della creazione della VM.
• Supporta lo standard Ethernet come un NIC fisico.

P . Belloni  | 
[I componentidella Rete Virtuale: Virtual HBA] 
18Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
• Abilita l’acceso di una VM al disco FC RDM/LUN assegnato alla VM stessa.
• Viene configurato usando la tecnologia N_Port ID Virtualization (NPIV).
▪ Un singolo FC HBA fisico o una porta CAN (N_Port) funziona come N porte
virtuali multiple, ognuna con il proprio world wide name (WWN, un indirizzo
univoco a 64-bit).
• Il kernel dell’hypervisor utilizza NPIV per instanziare N_porte virtuali, assegnadole
alle VM.


P . Belloni  | 
I componentidella Rete Virtuale: Virtual Switch 1/4 
19Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
• È uno switch logico che lavora al livello 2 della pila OSI e supporta il protocollo
Ethernet.
• Si trova all’interno di un server fisico.
• Viene creato e configurato usando l’hypervisor.
• Conserva una tabella con gli indirizzi MAC al fine di forwardare i pacchetti.
▪ MAC address table: MAC address + porta.
• Indirizza il traffico di rete verso/dalle VM e il kernel di hypervisor.
▪ VM verso VM internamente al server fisico.
▪ VM verso rete fisica.
▪ Hypervisor kernel: IP storage, VM migration e traffico di gestione.

P . Belloni  | 
I componentidella Rete Virtuale: Virtual Switch 2/4 
20Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
• Un virtual switch può essere connesso a diversi NIC fisici.
▪ La connessione a NIC diversi abilita il load balancing ed il failover del traffico
outbound.


P . Belloni  | 
I componentidella Rete Virtuale: Virtual Switch 3/4 
21Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
• Un virtual switch può non essere connesso ad alcun NIC fisico.
▪ In questo caso, indirizza il traffico di VM all’interno del server fisico (es.
firewall).


P . Belloni  | 
I componentidella Rete Virtuale: Virtual Switch 4/4 
22Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
• Non c’è mai connessione diretta tra virtual switch (peculiarità di Vmware; in altre
parole, VMware implementa un “single-tier networking”. Come conseguenza il
protocollo di spanning Tree per prevenire loop non serve) .
• Tuttavia il traffico può essere trasferito tra virtual switch attraverso le VM a questi
attestate.
• I NIC fisici permettono ai virtual switch di collegarsi alla rete fisica, per questo
motivo un NIC fisico non è condiviso tra diversi virtual switch.

P . Belloni  | 
Virtual Switch: porte e gruppi di porte
23Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
• Tipi di porte del virtual switch:
❑Hypervisor kernel port: garantiscono connettività al kernel di hypervisor;
❑VM port: forniscono connettività ai virtual NIC;
❑Uplink port: garantiscono connettività al NIC fisico. Un virtual switch è in grado di trasferire
dati ad una rete fisica solo se uno o più NIC fisici sono conessi alle sue uplink port.
• VM port group: raggruppare le porte delle VM è un meccanismo per applicare le stesse politiche
di rete (policy) a tutte le VM del Gruppo, invece di configurarle singolarmente su ogni porta.
▪ Esempi di politiche: sicurezza, load balancing, failover tra PNIC, limitazioni di banda.
• Le VM collegate ad un VM port group condividono la stessa configurazione.
▪ Evita di configurare le policy individualmente su ogni porta di VM.
VM port

P . Belloni  | 
Virtual Switch Distribuito
24Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
• È possible aggregare più virtual switch istanziati su diversi server fisici: questo
crea uno switch virtuale distribuito, che funziona come un singolo virtual switch.
• Solitamente, gli switch virtuali distribuiti permettono 1. di gestire in modo
centralizzato la rete di VM e 2. di mantenere le stesse politiche di rete in caso di
migrazione di VM tra server fisici.



---

# Virtualizzazione 26 - La Virtualizzazione

**File:** `Virtualizzazione 26 - La Virtualizzazione.pdf`
**Tipo:** `.pdf`
**Dimensione:** 1697.2 KB
**Ultima modifica:** 02/07/2026 09:12

---

Paolo BELLONI [paolo.belloni@its-ictpiemonte.it]DOCENTE
Sistemi di VirtualizzazioneUnità Formativa
Lez. 01 - VirtualizzazioneArgomento


Virtualizzazione | 
Esempio | La Macchina Host o Server Fisico
2
▪ Ciascuno dei due server IBM Flex
x440 è equipaggiato come segue:
➢24 core x86 a 2,7 GHz;
➢192 GB di RAM;
➢1 Fiber Channel HBA (Host Bus
Adapter) 16 Gbps;
➢8 porte Ethernet da 1 Gbps.
▪ La SAN si basa su SAN Brocade e
su un'unità IBM StorWize V7000
con 20 dischi SAS da 300 GB e 4
SSD da 250 GB.
▪ Flex FC 5022 è adattatore SAN
montato sul server.

Virtualizzazione | 
Esempio | I Server Virtuali
3
▪ Le macchine virtuali costituiscono tre ambienti:
➢ Produzione
➢ Test/Perf
➢ Development/Acceptance
▪ La potenza richiesta per le macchine (virtuali) è
stata stimata in un esercizio di sizing.
▪ La capacità complessiva del server fisico è
superiore alla somma delle macchine virtuali
configurate (33 core/cpu).
▪ È possibile osservare che la potenza delle
macchine di Acceptance/Dev e Test/Perf è simile o
uguale a quella dell’ambiente di Produzione.
▪ Questo perché la virtualizzazione consente di
presentare al richiedente, cioè la VM, la potenza
necessaria quando questa è necessaria.
▪ Nel caso di un ambiente fisico tutta la potenza
dovrebbe essere stata resa SEMPRE disponibile.


Virtualizzazione | 
Cloud Computing
▪ Definizione secondo U.S. National Institute of Standards and Technology (NIST).
“Cloud è un modello di accesso via rete da qualsiasi luogo, comodo e on-demand,
ad un insieme di risorse condivise – reti, server, dispositive di memorizzazione,
applicazioni e servizi – che possono essere forniti e rilasciati rapidamente, con
minimo costo di gestione o interazione con il fornitore del Servizio”.
▪ Caratteristiche dell’elaborazione in Cloud:
✓On demand (variazione di risorse "agile").
✓Shared resource pooling (risorse condivise).
✓Rapid elasticity (variazione di risorse "immediata").
✓Measured service (misura uso risorse / fatturaz. a consumo).
✓Broad network access.
✓High availability, disaster recovery (SLA).
4

Virtualizzazione | 
▪ Un data center è una struttura utilizzata per ospitare sistemi informatici e
componenti associati, come sistemi di telecomunicazione e archiviazione.
▪ Generalmente include alimentatori ridondanti o di backup, connessioni di
comunicazione dati ridondati, controlli ambientali (ad esempio, condizionamento
dell'aria, sistemi antincendio) e vari dispositivi di sicurezza.
▪ I grandi data center sono edifici su scala industriale che utilizzano tanta elettricità
quanto una piccola città.
Data Center
5

Virtualizzazione | 
Data Center – Un Sistema complesso
6


Virtualizzazione | 
Data Center – Non solo Computing
7


Virtualizzazione | 
Data Center - Condizionamento
8


Virtualizzazione | 
ll settore dei data center in Italia sta vivendo una fase di crescita senza
precedenti, come evidenziato dai dati dell’Osservatorio Data Center del
Politecnico di Milano. Nel 2024, la potenza energetica totale dei data
center italiani ha raggiunto i 513 MW IT, segnando un incremento del
17% rispetto all’anno precedente. Questo sviluppo è stato alimentato da
investimenti massicci: nel biennio 2023-2024 sono stati spesi 5 miliardi
di euro per la costruzione e l’allestimento di nuove infrastrutture,
mentre per il biennio 2025-2026 sono previsti ulteriori 10,1 miliardi di
investimenti.
OsservatorioData Center del POLIMI
9

Virtualizzazione | 
▪ Un Data Center Classico (Classic DC CDC) contiene risorse fisiche di Information
Technology che includono la risorse computazionali, la rete e lo storage.
Data Center Classico (CDC)
10Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011


Virtualizzazione | 
Business applications
▪ E-mail, Enterprise Resource Planning (ERP), Decision Support System (DSS),
Data Warehouse (DW).
Management applications
▪ Resource management, performance tuning.
Data protection applications
▪ Backup, replication.
Security applications
▪ Autenticazione, antivirus.
➢Caratterisitche principali di I/O per una applicazione
✓Read intensive vs. write intensive
✓Sequential vs. random
Applicazioni
11Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

Virtualizzazione | 
• Un database è un modo strutturato per memorizzare i dati in
tabelle logicamente organizzate e collegate tra loro.
➢ Un database aiuta a ottimizzare l’archiviazione e il recupero dei dati.
• Un Sistema di Gestione di Database (DBMS) è un insieme di
programmi che controllano la creazione, la manutenzione e l’uso
di un database.
➢ Il DBMS elabora la richiesta di dati di un’applicazione e istruisce il
sistema operativo per accedere ai dati appropriati.
➢ Il DBMS gestisce i dati in arrivo, li organizza e facilita la modifica o
l’estrazione dei dati da parte degli utenti o di altri programmi.
• Alcune soluzioni DBMS popolari sono MySQL, Oracle, SQL Server,
etc.
Database Management System
12Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

Virtualizzazione | 
Una risorsa che esegue le applicazioni con il supporto delle componenti
computazionali sottostanti.
▪ Consiste in componenti fisici (dispositivi hardware) che comunicano
tra loro utilizzando componenti logici (software e protocolli).
▪ Tre componenti fisici chiave: Unità di Elaborazione Centrale (CPU),
Memoria e dispositivi di Input/Output (I/O).
➢La memoria viene utilizzata per memorizzare i dati, sia in modo persistente
che temporaneo.
➢I dispositivi I/O consentono di inviare e ricevere dati da e verso un sistema di
calcolo. Questa comunicazione può essere di uno dei seguenti tipi:
✓Comunicazioni utente-compute: gestite da dispositivi I/O di base, come la tastiera, il
mouse e il monitor. Questi dispositivi consentono agli utenti di inserire dati e visualizzare
i risultati delle operazioni.
✓Comunicazioni compute-compute/archiviazione: gestite dal host controller o
dall'adattatore host (host adapter) che collega un sistema di calcolo a un altro sistema di
calcolo/dispositivo di archiviazione.
Compute
13Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

Virtualizzazione | 
HW | Esempi di Compute
14
• Laptop/desktop, blade server, complessi cluster di server, computer
mainframe, ecc.
• La tecnologia di blade server è comunemente utilizzata per
implementare il computer nei cDC.
• Sono stati sviluppati in risposta alla crescente necessità di una
potenza di calcolo che non occupi molto spazio.
• Riducendo i costi e la complessità nel datacenter, i blade server
consolidano le funzioni di alimentazione e di sistema in un unico
chassis integrato e consentono l'aggiunta di server come componenti
hot-pluggable.
• La tecnologia dei blade server aumenta notevolmente la densità dei
server, riduce i costi di alimentazione e raffreddamento, facilita
l'espansione dei server e semplifica la gestione del datacenter.
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

Virtualizzazione | 
Features and specifications
• Processors
✓Up to two Intel Xeon 2.8 or 3.6 GHz / 800 MHz
✓1MB L2 Cache
• Memory
✓Up to 8 GB PC2-3200
✓Four slots
• Hard drives
✓Up to Two 36.4 GB 10,000 rpm
✓Ultra320 SCSI
• Networking
✓Dual 10/100/1000 Ethernet controller /
Broadcom 5704S
• Video
✓ATI RadeonTM 7000M
HW | Esempi di Compute | Blade Server
15
Blade server IBM HS20
Frequenza di clock = 
velocità cui il processore
esegue le istruzioni
Bus di Sistema = velocità
alla quale I dati vengono
trasferiti tra processore e 
RAM  

Virtualizzazione | 
HW | Esempi di Compute | Blade Server
16


Virtualizzazione | 
HW | Server Clustering
17
• È il metodo di raggruppare due o più server (noti anche come nodi) e
farli lavorare insieme come un unico sistema.
• Questo garantisce che le applicazioni e le risorse mission-critical siano
altamente disponibili: più nodi vengono riuniti in un cluster per migliorare
la disponibilità e le prestazioni.
• Quando si verifica un guasto su un nodo in un cluster, le risorse vengono
reindirizzate e il carico di lavoro viene riassegnato a un altro nodo nel cluster.
• Il clustering si implementa con software che collega i nodi nel cluster
e fornisce una vista del sistema unico ai client che utilizzano il cluster
stesso.
• Questi nodi comunicano tra loro tramite una rete privata. La
comunicazione tra i nodi di un cluster tramite heartbeat consente al
servizio di clustering di rilevare i guasti dei nodi e i cambiamenti di
stato, e gestisce il cluster come un'unica entità.
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

Virtualizzazione | 
Storage
18
▪ È una risorsa che permette di immagazzinare i dati in modalità
persistente, per un uso successivo.
➢I dati creati da individui o aziende devono essere memorizzati in modo che siano
facilmente accessibili per ulteriori elaborazioni.
• I dispositivi progettati per memorizzare i dati sono chiamati dispositivi di
archiviazione o semplicemente storage.
• Il tipo di archiviazione utilizzato varia in base al tipo di dati ed alla velocità
con cui vengono creati e utilizzati.
➢Dispositivi come la memoria in un telefono cellulare o una fotocamera digitale, DVD,
CD-ROM e unità disco nei computer personali sono esempi di dispositivi di
archiviazione.
• Un dispositivo di archiviazione utilizza supporti magnetici, ottici o a stato
solido.
➢I dischi, i nastri e i dischetti utilizzano supporti magnetici.
➢I CD/DVD utilizzano supporti ottici per l'archiviazione.
➢La memoria flash rimovibile o le unità flash sono esempi di supporti a stato solido.
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

Virtualizzazione | 
Tipi di Storage
19Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011


Virtualizzazione | 
Network | Il Modello ISO OSI
20


Virtualizzazione | 
Virtualizzazione
• T = Hardware reale (Target)
• V = Virtual, Software eseguibile su HW
H, detto Host
• S = SW originariamente sviluppato per
T
➢Non si vuole cambiare S.
➢HW T non è più disponibile.
➢V è meno costoso di T.
➢V è più flessibile di T.
➢V rende il sistema che esegue S più
sicuro.
21


Virtualizzazione | 
Virtualizzazione
• Livello alto di astrazione di un sistema
che nasconde i dettagli
dell’implementazione sottostante.
• Astrazione di risorse computazionali:
❑si presenta all’utilizzatore una
vista logica diversa da quella
fisica.
• Come? Disaccoppiando l’architettura
ed il comportamento delle risorse hw
e sw percepiti dall’utente dalla loro
realizzazione fisica.
22
Sistema Reale
--- risorse HW e SW ---
Tecnologie di Virtualizzazione
Vista Logica (sistema virtuale)
Vista Fisica
(sistema reale)

Virtualizzazione | 
Virtualizzazionedi Risorse
• Virtualizzazione di Risorse
computazionali di Sistema (hw + sw)
• Macchina Virtuale (VM), container
• Virtualizzazione di Storage
• Storage Area Network (SAN)
• Virtualizzazione di Rete
• Virtual LAN (VLAN), Virtual Private
Network (VPN)
• Virtualizzazione di Data Center
23


Virtualizzazione | 
Il Cloud
24
• La virtualizzazione è il primo
passo verso la creazione di
un'infrastruttura Cloud.
• Trasformare un Data Center
classico (C-DC) in un Data
Center virtualizzato (V-DC)
richiede la virtualizzazione degli
elementi principali del Data
Center.
• Un approccio graduale alla
virtualizzazione di
un'infrastruttura consente una
transizione agevole da C-DC a V-
DC.
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

Virtualizzazione | 
Macchina Virtuale
• Una macchina virtuale (VM, Virtual
Machine, in contrapposizione ad una
macchina fisica o reale) permette di
rappresentare le risorse hw/sw di una
macchina diversamente dalla loro
realtà.
❖ Ad es.: risorse hw della VM (CPU, scheda di
rete, …) diverse dalle risorse fisiche della
macchina reale.
❖ Ad es.: risorse sw (sistema operativo, …)
diverse dalle risorse sw della macchina
reale.
• Una singola macchina fisica può
essere usata come differenti ambienti
di elaborazione.
❖ Molteplici VM su una singola macchina
fisica.
25
Hardware
Layer di Virtualizzazione
VM1 VMXVM2

Virtualizzazione | 
Cenni Storici sulla Virtualizzazione1/2
• Il concetto di VM è un’idea “vecchia” ,essendo stato definito a metà degli anni ’60
in un contesto centralizzato.
➢Ideato per consentire al software legacy (esistente) di essere eseguito su
mainframe molto costosi e condividere in modo trasparente le (scarse) risorse
fisiche.
➢Fu uso per la prima volta sul mainframe IBM System/360-67, basato su un
emulatore che i programmatori usavano per sviluppare un sistema operativo
(simile nel principio ma molto diverso nella realizzazione dall’attuale
virtualizzazione).
• Negli anni ’80, con il passaggio ai PC, il problema della condivisione trasparente
delle risorse di calcolo viene risolto dai SO multitasking.
➢L’interesse per la virtualizzazione svanisce.
26

Virtualizzazione | 
IBM System/360-67
27
1
2
3
4
5
6

Virtualizzazione | 
Cenni Storici sulla Virtualizzazione2/2
• Alla fine degli anni '90, l’interesse rinasce per rendere meno onerosa la
programmazione hw special-purpose.
✓VMware fondata nel 1998.
• Si acuisce il problema dei costi di gestione e di sottoutilizzo di piattaforme hw e
sw eterogenee.
✓L’hw cambia più velocemente del sw (middleware e applicazioni).
✓Aumenta il costo di gestione e diminuisce la portabilità.
• Diventa nuovamente importante la condivisione dell’hw e delle capacità di
calcolo non usate, per ridurre i costi dell’infrastruttura.
✓È una delle tecnologie abilitanti del Cloud Computing.
28

Virtualizzazione | 
I Vantaggidella Virtualizzazione1/3
• Facilita la compatibilità, portabilità, interoperabilità e migrazione di applicazioni
ed ambienti.
▪ Indipendenza dall’hw.
▪ Create Once, Run Anywhere.
▪ VM legacy: eseguire vecchi SO o vecchie applicazioni su nuove piattaforme.
29
Programma
Interfaccia A
Hardware/software Sistema A
Programma
Interfaccia B
Hardware/software Sistema B
Interfaccia A
Implementazione della
mimica A su B

Virtualizzazione | 
I Vantaggidella Virtualizzazione2/3
• Permette il consolidamento dei server (servers consolidation) in un data center,
con vantaggi economici, gestionali ed energetici.
✓Multiplexing di molteplici VM sullo stesso server.
✓Obiettivo: ridurre il numero totale di server usati, utilizzandoli in modo più
efficiente.
✓Vantaggi:
❑Riduzione di costi, consumi energetici e spazio occupato.
❑Semplificazione nella gestione, manutenzione ed upgrade dei server.
❑Riduzione dei tempi di downtime, tramite live migration di VM.
30

Virtualizzazione | 
Il Consolidamentodei Server
31
Server
SALES
Windows
HW
CRM
Linux
ERP
Solaris
Hardware
OS
Application
37%Utilizzo
Strato di 
Virtualizzazione
o Hypervisor

Virtualizzazione | 
I Vantaggidella Virtualizzazione3/3
• Permette di isolare componenti malfunzionanti o soggetti ad attacchi di sicurezza,
incrementando affidabilità e sicurezza delle applicazioni.
▪ Macchine virtuali di differenti applicazioni non possono avere accesso alle
rispettive risorse.
▪ Bug del software, crash, virus in una VM non possono danneggiare altre VM
in esecuzione sulla stessa macchina fisica.
• Permette di isolare le prestazioni di diverse VM.
▪ Tramite lo scheduling delle risorse fisiche che sono condivise tra molteplici
VM in esecuzione sulla stessa macchina fisica.
• Permette di bilanciare il carico sui server.
▪ Tramite la migrazione della VM da un server ad un altro.
32

Virtualizzazione | 
Uso di ambienti di esecuzione virtualizzati
• In ambito personale e didattico.
▪ Per eseguire simultaneamente diversi SO sulla stessa macchina.
▪ Per semplificare l’installazione di sw.
• In ambito professionale.
▪ Per debugging, testing e sviluppo di applicazioni.
• In ambito aziendale.
▪ Per consolidare l’infrastruttura del data center.
▪ Per garantire business continuity: incapsulando interi sistemi in singoli file
(system image) che possono essere replicati, migrati o reinstallati su qualsiasi
server.
33

Virtualizzazione | 
L’Hypervisor
• Un Hypervisor è un software di virtualizzazione che
permette di eseguire diversi SO
contemporaneamente sulla stessa macchina fisica,
interagendo direttamente con le risorse fisiche del
server.
• Un Hypervisor è un software che si trova tra il
sistema operativo e le risorse hw specializzate del
server.
• Quando è presente, è l’hypervisor, piuttosto che il
SO, che gestisce le connessioni tra i driver e le
risorse del server.
• L’hypervisor presenta una connessione virtuale alle
risorse del server per il SO di una VM.
• In particolare, l’hypervisor lo fa per molte VM in
esecuzione sullo stesso server, anche se queste VM
hanno tutte SO diversi e applicazioni non correlate
tra loro.
• Il termine hypervisor è una variante di supervisor
(solitamente riferito al kernel di un SO): essendo
l’hypervisor il supervisor di supervisor, il prefisso
hyper è una variante più forte di super.
• Il termine è stato usato per la prima volta attorno al
1970: IBM lo ha coniato per la macchina 360/65 e
successive. 34
SERVER
VM1 VM3VM2
Hypervisor
Driver
CPU
Driver Driver
NIC
Driver
DISKMemory
OS2 OS3
ApplicationApplication
OS1
Application


---

# Virtualizzazione 26 - VM e Openstack

**File:** `Virtualizzazione 26 - VM e Openstack.pdf`
**Tipo:** `.pdf`
**Dimensione:** 989.4 KB
**Ultima modifica:** 02/07/2026 09:25

---

Paolo BELLONI [paolo.belloni@its-ictpiemonte.it]DOCENTE
Sistemi di VirtualizzazioneUnità Formativa
Macchina Virtuale e OpenstackArgomento


P . Belloni  | 
InfrastrutturaVirtuale
Componenti software (softwarizzate, astratte) che abilitano l’esecuzione di
applicazioni senza disporre di una macchina fisica
• Macchine Virtuali
• Container
• K8S
• Cloud Service Provider
2

Openstack
3

P . Belloni  | 
▪ Attraverso software non troppo diverso da hypervisor, ma creato per
gestire il cloud.
▪ Orchestratore di macchina virtuali.
▪ Openstack: piattaforma software per il management di un cloud.
▪ Progetto iniziato nel 2010 dalla collaborazione tra Rackspace e la
NASA.
▪ Open source.
Come si realizza il Cloud Computing?
4

P . Belloni  | 
▪ Viene installato sul
VMM.
▪ Si avvale delle sue
funzionalità per creare
un cloud di macchine
fisiche
Come si realizza il Cloud Computing? (1)
5


P . Belloni  | 
Come si realizza il Cloud Computing? (2)
6


P . Belloni  | 
▪ Si avvale di libvirt:
▪ Layer per VMs
management (creare,
avviare, fermare,
modificare, monitorare,
migrare).
▪ Permette di interagire con
diversi VMM:
✓Kvm/Qemu,
✓Xen,
✓Vmware ESX,
✓MS Hyper-V
✓…
Libvirt per gestire eterogeneità
7


Gestione delle Risorse in Pool
8

P . Belloni  | 
La Gestione delle Risorse (Resource Management)
9Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
Un processo per allocare, a favore delle macchine virtuali (VM), le risorse di una
macchina fisica o di un cluster di macchine fisiche, al fine di ottimizzare l’utilizzo
complessivo delle risorse.
• A cosa serve la gestione delle risorse?
▪ Controlla l’uso delle risorse.
▪ Impedisce che una singola VM monopolizzi le risorse.
▪ Alloca le risorse opportunamente, in base alle priorità assegnate alle varie VM.
• Le risorse devono essere messe in pool (Resource Pooling), allo scopo di gestirle
“centralmente”.
• Risorse = CPU, memoria, rete e storage.
Resource Management

P . Belloni  | 
Il Resource Pooling
10Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
È una astrazione logica delle risorse fisiche aggregate, che ne abilita la gestione
centralizzata.
• Un pool è creato a partire da una macchina fisica o da un insieme di machine fisiche (cluster).
▪ Questo resource pool di partenza è definito parent resource pool.
• A partire dal parent resource pool (iniziale), gli Amministratori di sistema possono allocare le
risorse ad una applicazione o a delle VM.
▪ Le risorse allocate, a partire dal parent pool, per una specifica applicazione o alla singola VM si definiscono
child resource pool.
• Tre indicatori vengono usati per controllare le risorse consumate dai diversi pool o dalle VM.
• Si parla di Key Performance Indicator (KPI). Questi sono:
• Reservation;
• Limit;
• Share.
Resource Pooling

P . Belloni  | 
Il Resource Pooling: un esempio
11Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011


P . Belloni  | 
Share, Limit e Reservation
12Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
• Share Limit e Reservation sono dei parametri (variabili) che controllano le risorse allocate
ed utilizzate da un child resource pool o da una VM.
❖Share
▪ Quantità di CPU o memoria che una VM o un child pool può avere, rispetto al totale delle
risorse (di CPU o memoria) del parent pool.
▪ Individua la priorità di una VM o child pool.
❖Limit
▪ Massima quantità di CPU o memoria che una VM o un child pool può consumare.
▪ Configurato alla creazione della VM, si può modificare solo a VM spenta.
❖Reservation
▪ Quantità di CPU o memoria riservata per una VM o per un child pool.
▪ Una VM non viene attivata, se la quanità di risorse definite dalla reservation non sono
disponibili.
▪ Se la VM non utilizza tutte le risorse riservate, quelle libere vengono allocate ad altre
VM.

P . Belloni  | 
L’ottimizzazionedelle risorse di CPU
13Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
• Allocare le risorse di una CPU in modo efficiente e appropriato è fondamentale.
• Le moderne CPU sono equipaggiate con core multipli e con hyper-threading.
▪ I processori multi-core hanno, in una singola CPU (circuito integrato o socket),
diverse unità di processamento (processing unit, a.k.a. core).
▪ L’hyper-threading fa apparire una CPU fisica come due o più CPU logiche.
• L’hypervisor definisce e alloca le CPU virtuali sulla CPU fisiche (analogamente a
come un SO assegna ai diversi processi – o thread – il tempo di CPU).
• L’hypervisor supporta le funzionalità di multi-core, hyper-threading e CPU load-
balancing (bilanciamento del carico) per ottimizzare le risorse della CPU.

CPU: pCPU, L-CPU, vCPU
14

P . Belloni  | 
I processori Multi-Core
15Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011


P . Belloni  | 
Un thread o thread di esecuzione, in informatica, è una
suddivisione di un processo in due o più filoni (istanze) o
sottoprocessi, che vengono eseguiti simultaneamente da
un sistema di elaborazione monoprocessore (mono-
threading) o multiprocessore (multi-threading)
o multicore.
L’hyper-threading
• L’hyper-threading fa apparire una CPU come due CPU
logiche (Logical CPU LCPU).
▪ In pratica, l’hyper-threading abilita il SO a eseguire due
o piu thread contemporaneamente.
• Due LCPU condividono le stesse risorse fisiche.
▪ Due thread non possono essere eseguiti
contemporaneamente, ma mentre un thread è bloccato,
la CPU può eseguire una altro thread.
• L’hypervisor in esecuzione su una CPU che supporta
hyper-threading ha prestazioni migliori ed un utilizzo
delle risorse più efficiente.
16Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011


P . Belloni  | 
Il bilanciamentodi carico della CPU
17Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
• Un aspetto fondamentale della gestione
delle risorse è il bilanciamento del carico
(load balancing) tra le risorse di
processamento disponibili nella particolare
configurazione considerata.
• Diventa chiave nel caso di sistema multi-
processore e in caso l’hyper-threading sia
attivo.
▪ Un thread viene migrato da una L-CPU
troppo utilizzata verso una meno carica.
▪ L’hypervisor controlla ad intervalli regolari il
carico delle varie L-CPU, al fine di
mantenerlo bilanciato.
▪ Se una L-CPU non è utilizzata, viene
stoppata. Questo permette di liberare le
risorse fisiche della CPU e permette alla VM
in esecuzione sulla L-CPU dello stesso core di
avere più “banda” disponibile.

P . Belloni  | 
Gestione della CPU nella VM
18
▪ L'hypervisor assegna gli intervalli di tempo sui
processori disponibili nel server host fisico per
l'esecuzione delle istruzioni delle CPU virtuali,
che indicheremo con vCPU.
➢ La prima vCPU deve eseguire una serie di
comandi sull'hardware virtuale e tale richiesta
viene indirizzata all'hypervisor.
➢ L'hypervisor schedula una sessione di
esecuzione per la richiesta di quella vCPU (1).
➢ La CPU fisica esegue le istruzioni, restituisce i
risultati all'hypervisor, che li restituisce alla
prima macchina virtuale (2).
➢ Quindi l'hypervisor assegna l'esecuzione della
successiva serie di istruzioni dalla seconda
macchina virtuale (3) e (4).
▪ Inoltre, le CPU virtuali non sono associate a
CPU fisiche.
▪ Un hypervisor pianificherà il lavoro per conto
di una macchina virtuale su qualsiasi CPU
fisica disponibile.
DISK

P . Belloni  | 
Gestione della CPU nella VM
19
▪ La tabella mostra il numero di core
disponibili in funzione delle
configurazioni del processore e del
numero di processori.
▪ Ogni vendor di sistemi di
virtualizzazione dichiara il rapporto
max vCPU/CPU.
▪ Ogni guest utilizza una parte di una
CPU fisica e quindi si può allocare più
di una vCPU per ogni CPU fisica del
server.
▪ Ogni fornitore ha le proprie indicazioni
sul massimo numero di vCPU che
possono essere allocate su ogni
singolo host.


P . Belloni  | 
Gestione Quanti di Tempo vCPU
20
▪ L’hypervisor gestisce le
risorse della macchina fisica
esattamente come un
sistema operativo.
▪ La differenza è che le
richieste arrivano
all’hypervisor da un sistema
operativo installato su di
una vCPU.


VM – Esempio
21

P . Belloni  | 
Esempio | La Macchina Host o Server Fisico
22
▪ Ciascuno dei due server IBM Flex
x440 è equipaggiato come segue:
➢24 core x86 a 2,7 GHz;
➢192 GB di RAM;
➢1 Fiber Channel HBA (Host Bus
Adapter) 16 Gbps;
➢8 porte Ethernet da 1 Gbps.
▪ La SAN si basa su SAN Brocade e
su un'unità IBM StorWize V7000
con 20 dischi SAS da 300 GB e 4
SSD da 250 GB.
▪ Flex FC 5022 è adattatore SAN
montato sul server.

P . Belloni  | 
Esempio | I Server Virtuali
23
▪ Le macchine virtuali costituiscono tre ambienti:
➢ Produzione
➢ Test/Perf
➢ Development/Acceptance
▪ La potenza richiesta per le macchine (virtuali) è
stata stimata in un esercizio di sizing.
▪ La capacità complessiva del server fisico è
superiore alla somma delle macchine virtuali
configurate (33 core/cpu).
▪ È possibile osservare che la potenza delle
macchine di Acceptance/Dev e Test/Perf è simile o
uguale a quella dell’ambiente di Produzione.
▪ Questo perché la virtualizzazione consente di
presentare al richiedente, cioè la VM, la potenza
necessaria quando questa è necessaria.
▪ Nel caso di un ambiente fisico tutta la potenza
dovrebbe essere stata resa SEMPRE disponibile.


VM – Dimensionamento
24

P . Belloni  | 
vCPU | Esempio
25
Quante vCPU sono disponibili su CPU Intel® Xeon® Gold 6148, 2.4 GHz, 2 processors 20
core?
• Numero core totali = 2 x 20 = 40 CPU fisiche (pCPU).
• Senza hyperthreading → 40 vCPU disponibili (1vCPU = 1 thread HW).
• Con hyperthreading → 40 x 2 vCPU = 80 vCPU disponibili (1 vCPU = 1 LCPU).
• Il VMM può praticare l’overcommit di CPU, ovvero assegna complessivamente più vCPU
ai guest di quante pCPU fisiche siano disponibili, confidando nel fatto che non tutte le
vCPU richiedano tempo di esecuzione simultaneamente.
• In questo modo, le vCPU disponibili possono essere comunemente 80-160 senza degrado
prestazionale evidente.
• Si tenga presente che anche hypervisor usa risorse della macchina host, in questo caso
utilizza pCPU.
➢ Storicamente, si stimava un impatto sulla pCPU pari al 20% della capacita totale ma negli
hypervisor recenti si stima un impatto di hypervisor pari al 5% - 10% di pCPU (10% nel caso di VM-
exit molto frequenti).
➢ Nel nostro caso, le pCPU disponibili diventano 40 x 0.95 = 38 pCPU (che diventano 36 pCPU se
overhead di hypervisor stiamato pari al 10%).

P . Belloni  | 
vRAM | Esempio 1/3 
26
Quanta vRAM può essere complessivamente assegnata a machine virtuali da VMM
su CPU Intel® Xeon® Gold 6148, 2.4 GHz, 2 processors 20 core, ipotizzando che su
ciascun blade server siano installati 256 GB di RAM fisica?
• pRAM = 256 GB.
• Il VMM può praticare l’overcommit di RAM, ovvero assegna complessivamente
più vRAM ai guest di quanta pRAM sia disponibile, confidando nel fatto che non
tutte le VM richiedano simultaneamente la quantita di RAM definita nel
paramento reservation.
• In questo modo, la quantità di vRAM disponibile può essere comunemente 1.2 – 1.5 volte
superiore alla pRAM installata, senza degrado prestazionale evidente.
• NOTA: mentre nel caso di CPU overcommit il degrado prestazionale e’ graduale, quando si
pratica RAM overcommit oltre il 1.5 questo innesca memory swap frequenti, che comportano
un degrado netto ed immediato delle prestazioni.

P . Belloni  | 
vRAM | Esempio 2/3 
27
Quanta vRAM può essere complessivamente assegnata a machine virtuali da VMM su CPU
Intel® Xeon® Gold 6148, 2.4 GHz, 2 processors 20 core, ipotizzando che su ciascun blade
server siano installati 256 GB di RAM fisica?
• pRAM = 256 GB.
• Come per CPU, hypervisor occupa RAM, in quanto:
➢ programma in esecuzione e quindi residente in RAM (architettura di von Neumann);
➢ con strutture dati di controllo per gestire e controllare le VM;
✓ stato di VM,
✓ stato di vCPU (registri e scheduling), p.es. VMCS/VMCB,
✓ configurazione delle VM;
➢ page table/EPT/NPT;
➢ buffer interni, cahce, networking.
➢ Storicamente, si stimava un impatto sulla pRAM pari al 20% della capacità totale ma negli
hypervisor recenti si stima un impatto di hypervisor pari al 5% - 10% (tale overhead è
sostanzialmente indipendente dalla frequenza delle VM-exit, che incidono invece sul consumo di
CPU).

P . Belloni  | 
vRAM | Esempio 3/3 
28
Quanta vRAM può essere complessivamente assegnata a machine virtuali da VMM
su CPU Intel® Xeon® Gold 6148, 2.4 GHz, 2 processors 20 core, ipotizzando che su
ciascun blade server siano installati 256 GB di RAM fisica?
• pRAM = 256 GB.
Soluzione.
1. Hypervisor overhead → pRAM effettivamente disponibile = 256 GB x 0.95 = 230
GB
2. RAM overcommit “prudente” → pRAM * 1.3 = 300 GB

