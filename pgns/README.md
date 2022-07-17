# pgn_to_json.py
  A simple tool to read PGN(Portable Game Notation) to JSON

  ##### Why another pgn reader?
  Because Why Not!
  I also just forgot to simply google search "python pgn reader" before making this.
  ##### Important Note
  Reads only the most basic of PGNs
  ##### BONUS!
  `json_to_mongodb.py` will load json to a mongodb. Use `python3 json_to_mongodb.py -h` for more information!   
  *This extra bonus script requires [PyMongo](https://pymongo.readthedocs.io/en/stable/)™. Terms and Conditions may apply.*


  ### Usage
  ---
  Simply run with a specified PGN file to output JSON to standard out
  > python3 pgn_to_json.py example_pgn.pgn
  >
  or specify an output file with the `-f` or `--file` flag!
  > python3 pgn_to_json.py example_pgn.pgn -f example_output_json.json
  >
  if you ever forget these complex instructions use the `-h` or `--help` flag

  ### Refrences
  ---
  - [Wiki on PGNs](https://en.wikipedia.org/wiki/Portable_Game_Notation)
  - [PGN Specification](https://github.com/mliebelt/pgn-spec-commented/blob/main/pgn-specification.md)
