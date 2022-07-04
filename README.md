# Jira Analytics

## Available commands
* Load issues into a database with the given project type
  ```
  ./cli.sh load --map map_ol "project = OL" --max-results 500
  ```
  ```
  ./cli.sh load --map map_bac  "project = BAC  and created >= 2019-01-01" --max-results 100000
  ./cli.sh load --map map_plat "project = PLAT and created >= 2019-01-01" --max-results 100000
  ./cli.sh load --map map_arch "project = ARCH and created >= 2019-01-01" --max-results 100000
  ./cli.sh load --map map_cu   "project = CU   and created >= 2019-01-01" --max-results 100000
  ./cli.sh load --map map_TWR  "project = TWR  and created >= 2019-01-01" --max-results 100000

  ```
  ```
  ./cli.sh load --map map_bac "project = BAC  and created >= 2019-01-01" --max-results 1 --batch-size 1 --no-save
  ./cli.sh load --map map_ilv "key = ILV-4977" --max-results 1 --batch-size 1 --no-save
  ./cli.sh load --map map_ol  "key = OL-249"   --max-results 1 --batch-size 1 --no-save
  ```
* Show information about a specific issue
  ```
  ./cli.sh search "key=BAC-5948" --max-results 1 --flatten
  ```
* Configure the default database
  ```
  ./cli.sh config db ~/jira.db
  ```
* Show configuration
  ```
  /cli.sh config show
  ```
* Load changelog
  ```
  ./cli.sh changelog all --max-results 100
  ```

## Reporting
* Run SQL queries
  ```
  $ ./cli.sh sql ./sql/queries/issue_lifecycle.sql
  ```
* Run report
  ```
  $ ./cli.sh report --param crunch_date "2020-01-01" "issue_timeline"
  ```
## JQL examples
* Issues worked on during specific dates
  ```
  (updated >= 2021-01-01 AND updated < 2022-01-01 OR resolutiondate >= 2021-01-01 AND resolutiondate < 2022-01-01) 
  ORDER BY resolution ASC, resolved DESC, created DESC
  ```

## JIRA API references
* https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-issueidorkey-changelog-get
* https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/#api-rest-api-3-search-post
* https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/