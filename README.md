# Jira Analytics

## Available commands
* Load issues into a database with the given project type
  ```
  ./cli.sh load --map map_ol "project = OL" --max_results 400
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
  ./cli.sh load --map map_ilv "key = ILV-4977 and created >= 2019-01-01" --max-results 1 --batch-size 1 --no-save
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

## JQL examples
* Issues worked on during specific dates
  ```
  (updated >= 2021-01-01 AND updated < 2022-01-01 OR resolutiondate >= 2021-01-01 AND resolutiondate < 2022-01-01) 
  ORDER BY resolution ASC, resolved DESC, created DESC
  ```
* 