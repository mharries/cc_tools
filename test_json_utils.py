import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    #Loop through the json_data
    for game in json_data["games"]:
        #Create a new Game object from the json_data by reading
        new_game = test_data.Game()
        #  title
        new_game.title = game["title"]

        #  year
        new_game.year = game["Year"]
        #  platform (which requires reading name and launch_year)
        new_platform = test_data.Platform()
        platform_data = game["platform"]
        new_platform.launch_year = platform_data["launch year"]
        new_platform.name = platform_data["name"]
        new_game.platform = new_platform
        #Add that Game object to the game_library
        game_library.add_game(new_game)
    #Return the completed game_library
    return game_library
