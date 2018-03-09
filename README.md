[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/magland/notebooks/master?filepath=mlstudy.ipynb)

## MLStudy Notebook Integration (WIP)
Providing jupyter notebooks for exploration of datasets in MLStudy.

kubespawner/dockerspawner are plugins to JupyterHub that uses kubernetes to manage containers containing notebook instances.

Potential Event Flows
Option 1
User requests notebook -> Lari API -> Original Processing Container returns the location where its persistent storage is mounted -> spawner gives us a new container with a single user notebook *that mounts the same persistent storage as the processing container*. -> Lari API -> return url where notebook is running

Option 2
User requests notebook -> spawner creates container running notebook & container could pre-load all/some data from study via KBucket (either the actual data or just .prv) -> Lari API  -> return url where notebook is running

Option 3
User requests notebook -> spawner creates container running notebook --> Lari API  -> return url where notebook is running --> User runs a command at the start of the notebook to pull the data (would require an API for each language)

Either way we could also provide a link to the docker image that has been built which could include both the (links to) the data and the notebook so a user can download it and run themselves if they want.

Security/Auth
- Fine-grained control over the resuources to be allocated are part of JupyterHub/K8s
- Auth can either be via url (By default JHub gives you a url with the token included)
- Probably best to set a max up-time for each of the notebooks (free with kubespawner)
