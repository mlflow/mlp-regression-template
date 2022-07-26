## What changes are proposed in this pull request?

(Please fill in changes proposed in this fix)

## How is this patch tested?

(Details)

We require adding a link to the [workflow](https://github.com/mlflow/mlflow/actions/workflows/pipeline-template.yml) for testing the [mlflow/mlp-regression-template](https://github.com/mlflow/mlp-regression-template) code path.

Run the workflow with repository name: `mlflow/mlp-regression-template` and the branch`(Example:<user-name>:feature)` that you are working with.
## Release Notes

### Is this a user-facing change?

- [ ] No. You can skip the rest of this section.
- [ ] Yes. Give a description of this change to be included in the release notes for MLflow users.

(Details in 1-2 sentences. You can just refer to another PR with a description if this PR is part of a larger change.)

### What component(s), interfaces, languages, and integrations does this PR affect?
Components
- [ ] `area/regression`: Sklearn regression pipeline example
- [ ] `area/build`: Build and test infrastructure for MLflow pipeline example

<!--
Insert an empty named anchor here to allow jumping to this section with a fragment URL
(e.g. https://github.com/mlflow/mlflow/pull/123#user-content-release-note-category).
Note that GitHub prefixes anchor names in markdown with "user-content-".
-->
<a name="release-note-category"></a>
### How should the PR be classified in the release notes? Choose one:

- [ ] `rn/breaking-change` - The PR will be mentioned in the "Breaking Changes" section
- [ ] `rn/none` - No description will be included. The PR will be mentioned only by the PR number in the "Small Bugfixes and Documentation Updates" section
- [ ] `rn/feature` - A new user-facing feature worth mentioning in the release notes
- [ ] `rn/bug-fix` - A user-facing bug fix worth mentioning in the release notes
- [ ] `rn/documentation` - A user-facing documentation change worth mentioning in the release notes
