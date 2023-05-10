import cv2
import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import numpy as np
from stockfish import Stockfish
import io
import pyautogui
import time

stockfish = Stockfish("StockFish/stockfish_13_win_x64_bmi2.exe")
stockfish.set_depth(10)
stockfish.set_skill_level(20)
board_region = (590, 165, 680, 670)
BBishop_img = cv2.imread('BlackPieces/BBishop.jpg')
BKing_img = cv2.imread('BlackPieces/BKing.jpg')
BKnight_img = cv2.imread('BlackPieces/BKnight.jpg')
BPawn_img = cv2.imread('BlackPieces/Bpawn.jpeg')
BQueen_img = cv2.imread('BlackPieces/BQueen.jpg')
BRook_img = cv2.imread('BlackPieces/BRook.jpg')

WBishop_img = cv2.imread('WhitePieces/WBishop.jpg')
WKing_img = cv2.imread('WhitePieces/WKing.jpeg')
WKnight_img = cv2.imread('WhitePieces/WKnight.jpeg')
WPawn_img = cv2.imread('WhitePieces/Wpawn.jpeg')
WQueen_img = cv2.imread('WhitePieces/WQueen.jpg')
WRook_img = cv2.imread('WhitePieces/WRook.jpg')

while True:
    # Capture screenshot of the chessboard region
    screenshot = pyautogui.screenshot(region=board_region)
    screenshot.save("board.jpg")

    # Load the captured region as "board_img"
    board_img = cv2.imread('board.jpg')
    
    #Empty Squares
    def filter_duplicates(locations, threshold):
        filtered = []
        for loc in locations:
            x1, y1, _, _ = loc
            unique = True
            for filtered_loc in filtered:
                x2, y2, _, _ = filtered_loc
                distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                if distance < threshold:
                    unique = False
                    break
            if unique:
                filtered.append(loc)
        return filtered
    def is_inside_polygon(point, polygon):
        return polygon.contains(Point(point[0], point[1]))

    distance_threshold = 50
    spaces = []
    for row in range(8):
        for col in range(8):
            space = chr(ord('h') - col) + str(row + 1)
            spaces.append(space)

    Polygons = []

    for row in range(8):
        for col in range(8):
            x1 = col * 85
            y1 = row * 85
            x2 = x1 + 85
            y2 = y1 + 85
            
            polygon = Polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)])
            Polygons.append(polygon)
    polygonlist = list(Polygons)


    all_pieces = []
    class BlackPieces:
        def __init__(self, BBishop_img, BKing_img, BKnight_img, BPawn_img, BQueen_img, BRook_img):
            self.BBishop_img = BBishop_img
            self.BKing_img = BKing_img
            self.BKnight_img = BKnight_img
            self.BPawn_img = BPawn_img
            self.BQueen_img = BQueen_img
            self.BRook_img = BRook_img

        #BlackBishops
        BlackBishops = cv2.matchTemplate(board_img, BBishop_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(BlackBishops)
        yloc, xloc = np.where(BlackBishops >= .8)
        Black_bishop_locations = []

        for (x, y) in zip(xloc, yloc):
            cv2.rectangle(board_img, (x, y), (x + 50, y + 50), (255, 255, 0), 2)
            Black_bishop_locations.append([x, y, x + 50, y + 50])
        Black_bishop_locations = filter_duplicates(Black_bishop_locations, distance_threshold)
        # Group the rectangles if desired
        rect, weights = cv2.groupRectangles(Black_bishop_locations, 1, 0.5)
        # for space, polygon in zip(spaces, Polygons):
        #     if polygon.contains(rect[i]):
        #         print(space + " " + str(polygon))
        #         print("Point" + " " + str(Point(int(x), int(y))))
        for bishop in Black_bishop_locations:
            for space, polygon in zip(spaces, Polygons):
                if is_inside_polygon((bishop[0] + 25, bishop[1] + 25), polygon):
                    all_pieces.append(space + " " + "b")




        #BlackKing
        BlackKing = cv2.matchTemplate(board_img, BKing_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(BlackKing)
        yloc, xloc = np.where(BlackKing >= .6)
        Black_king_locations = []
        for (x, y) in zip(xloc, yloc):
            cv2.rectangle(board_img, (x, y), (x + 50, y + 50), (255,0,255), 2)
            Black_king_locations.append([x, y, x + 50, y + 50])
        Black_king_locations = filter_duplicates(Black_king_locations, distance_threshold)
        rect, weights = cv2.groupRectangles(Black_king_locations, 1, 0.5)
        for king in Black_king_locations:
            for space, polygon in zip(spaces, Polygons):
                if is_inside_polygon((king[0] + 25, king[1] + 25), polygon):
                    all_pieces.append(space + " " + "k")

        #BlackKnights
        BlackKnights = cv2.matchTemplate(board_img, BKnight_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(BlackKnights)
        yloc, xloc = np.where(BlackKnights >= .7)
        Black_Knight_locations = []
        for (x, y) in zip(xloc, yloc):
            cv2.rectangle(board_img, (x, y), (x + 50, y + 50), (255,0,0), 2)
            Black_Knight_locations.append([x, y, x + 50, y + 50])
        Black_Knight_locations = filter_duplicates(Black_Knight_locations, distance_threshold)
        rect, weights = cv2.groupRectangles(Black_Knight_locations, 1, 0.5)
        for knight in Black_Knight_locations:
            for space, polygon in zip(spaces, Polygons):
                if is_inside_polygon((knight[0] + 25, knight[1] + 25), polygon):
                    all_pieces.append(space + " " + "n")





        #BlackPawns
        BlackPawns = cv2.matchTemplate(board_img, BPawn_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(BlackPawns)
        yloc, xloc = np.where(BlackPawns >= .8)
        Black_Pawn_locations = []
        for (x, y) in zip(xloc, yloc):
            cv2.rectangle(board_img, (x, y), (x + 50, y + 50), (0,255,0), 2)
            Black_Pawn_locations.append([x, y, x + 50, y + 50])
        Black_Pawn_locations = filter_duplicates(Black_Pawn_locations, distance_threshold)
        rect, weights = cv2.groupRectangles(Black_Pawn_locations, 1, 0.5)
        for pawn in Black_Pawn_locations:
            for space, polygon in zip(spaces, Polygons):
                if is_inside_polygon((pawn[0] + 25, pawn[1] + 25), polygon):
                    all_pieces.append(space + " " + "p")



        #BlackQueens
        BlackQueens = cv2.matchTemplate(board_img, BQueen_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(BlackQueens)
        yloc, xloc = np.where(BlackQueens >= .45)
        Black_Queen_locations = []
        for (x, y) in zip(xloc, yloc):
            cv2.rectangle(board_img, (x, y), (x + 50, y + 50), (100,100,100), 2)
            Black_Queen_locations.append([x, y, x + 50, y + 50])
        Black_Queen_locations = filter_duplicates(Black_Queen_locations, distance_threshold)
        rect, weights = cv2.groupRectangles(Black_Queen_locations, 1, 0.5)
        for queen in Black_Queen_locations:
            for space, polygon in zip(spaces, Polygons):
                if is_inside_polygon((queen[0] + 25, queen[1] + 25), polygon):
                    all_pieces.append(space + " " + "q")



        #BlackRooks
        BlackRooks = cv2.matchTemplate(board_img, BRook_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(BlackRooks)
        yloc, xloc = np.where(BlackRooks >= .8)
        Black_Rook_locations = []
        for (x, y) in zip(xloc, yloc):
            cv2.rectangle(board_img, (x, y), (x + 50, y + 50), (0,0,0), 2)
            Black_Rook_locations.append([x, y, x + 50, y + 50])
        Black_Rook_locations = filter_duplicates(Black_Rook_locations, distance_threshold)
        rect, weights = cv2.groupRectangles(Black_Rook_locations, 1, 0.5)
        for rook in Black_Rook_locations:
            for space, polygon in zip(spaces, Polygons):
                if is_inside_polygon((rook[0] + 25, rook[1] + 25), polygon):
                    all_pieces.append(space + " " + "r")


    class WhitePieces:
        def __init__(self, WBishop_img, WKing_img, WKnight_img, WPawn_img, WQueen_img, WRook_img):
            self.WBishop_img = WBishop_img
            self.WKing_img = WKing_img
            self.WKnight_img = WKnight_img
            self.WPawn_img = WPawn_img
            self.WQueen_img = WQueen_img
            self.WRook_img = WRook_img
        #WhiteBishops
        WhiteBishops = cv2.matchTemplate(board_img, WBishop_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(WhiteBishops)
        yloc, xloc = np.where(WhiteBishops >= .4)
        white_bishop_locations = []
        for (x, y) in zip(xloc, yloc):
            cv2.rectangle(board_img, (x, y), (x + 50, y + 50), (255,255,0), 2)
            white_bishop_locations.append([x, y, x + 50, y + 50])
        white_bishop_locations = filter_duplicates(white_bishop_locations, distance_threshold)
        rect, weights = cv2.groupRectangles(white_bishop_locations, 1, 0.5)
        for bishop in white_bishop_locations:
            for space, polygon in zip(spaces, Polygons):
                if is_inside_polygon((bishop[0] + 25, bishop[1] + 25), polygon):
                    all_pieces.append(space + " " + "B")

        #WhiteKing
        WhiteKing = cv2.matchTemplate(board_img, WKing_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(WhiteKing)
        yloc, xloc = np.where(WhiteKing >= .4)
        white_king_locations = []
        for (x, y) in zip(xloc, yloc):
            cv2.rectangle(board_img, (x, y), (x + 50, y + 50), (255,0,255), 2)
            white_king_locations.append([x, y, x + 50, y + 50])
        white_king_locations = filter_duplicates(white_king_locations, distance_threshold)
        rect, weights = cv2.groupRectangles(white_king_locations, 1, 0.5)
        for king in white_king_locations:
            for space, polygon in zip(spaces, Polygons):
                if is_inside_polygon((king[0] + 25, king[1] + 25), polygon):
                    all_pieces.append(space + " " + "K")

        #WhiteKnights
        WhiteKnights = cv2.matchTemplate(board_img, WKnight_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(WhiteKnights)
        yloc, xloc = np.where(WhiteKnights >= .5)
        white_knight_locations = []
        for (x, y) in zip(xloc, yloc):
            cv2.rectangle(board_img, (x, y), (x + 50, y + 50), (255,0,0), 2)
            white_knight_locations.append([x, y, x + 50, y + 50])
        white_knight_locations = filter_duplicates(white_knight_locations, distance_threshold)
        rect, weights = cv2.groupRectangles(white_knight_locations, 1, 0.5)
        for knight in white_knight_locations:
            for space, polygon in zip(spaces, Polygons):
                if is_inside_polygon((knight[0] + 25, knight[1] + 25), polygon):
                    all_pieces.append(space + " " + "N")

        #WhitePawns
        WhitePawns = cv2.matchTemplate(board_img, WPawn_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(WhitePawns)
        yloc, xloc = np.where(WhitePawns >= .5)
        white_pawn_locations = []
        for (x, y) in zip(xloc, yloc):
            cv2.rectangle(board_img, (x, y), (x + 50, y + 50), (0,0,255), 2)
            white_pawn_locations.append([x, y, x + 50, y + 50])
        white_pawn_locations = filter_duplicates(white_pawn_locations, distance_threshold)
        rect, weights = cv2.groupRectangles(white_pawn_locations, 1, 0.5)
        for pawn in white_pawn_locations:
            for space, polygon in zip(spaces, Polygons):
                if is_inside_polygon((pawn[0] + 25, pawn[1] + 25), polygon):
                    all_pieces.append(space + " " + "P")
        #WhiteQueens
        WhiteQueens = cv2.matchTemplate(board_img, WQueen_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(WhiteQueens)
        yloc, xloc = np.where(WhiteQueens >= .7)
        white_queen_locations = []
        for (x, y) in zip(xloc, yloc):
            cv2.rectangle(board_img, (x, y), (x + 50, y + 50), (0,255,0), 2)
            white_queen_locations.append([x, y, x + 50, y + 50])
        white_queen_locations = filter_duplicates(white_queen_locations, distance_threshold)
        rect, weights = cv2.groupRectangles(white_queen_locations, 1, 0.5)
        for queen in white_queen_locations:
            for space, polygon in zip(spaces, Polygons):
                if is_inside_polygon((queen[0] + 25, queen[1] + 25), polygon):
                    all_pieces.append(space + " " + "Q")

        #WhiteRooks
        WhiteRooks = cv2.matchTemplate(board_img, WRook_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(WhiteRooks)
        yloc, xloc = np.where(WhiteRooks >= .4)
        white_rook_locations = []
        for (x, y) in zip(xloc, yloc):
            cv2.rectangle(board_img, (x, y), (x + 50, y + 50), (0,0,0), 2)
            white_rook_locations.append([x, y, x + 50, y + 50])
        white_rook_locations = filter_duplicates(white_rook_locations, distance_threshold)
        rect, weights = cv2.groupRectangles(white_rook_locations, 1, 0.5)
        for rook in white_rook_locations:
            for space, polygon in zip(spaces, Polygons):
                if is_inside_polygon((rook[0] + 25, rook[1] + 25), polygon):
                    all_pieces.append(space + " " + "R")


    def white_king_side_castle_possible(board):
        # Check if the white king is in the correct starting position
        if board[7][4] != "K":
            return False

        # Check if the white king's rook is in the correct starting position
        if board[7][7] != "R":
            return False

        # Check if the squares between the king and rook are empty
        if any(board[7][i] != "." for i in range(5, 7)):
            return False

        # Check if the squares the king passes over are not under attack
        if any(is_square_attacked(board, 7, i, "black") for i in range(4, 7)):
            return False

        return True


    def white_queen_side_castle_possible(board):
        # Check if the white king is in the correct starting position
        if board[7][4] != "K":
            return False

        # Check if the white queen's rook is in the correct starting position
        if board[7][0] != "R":
            return False

        # Check if the squares between the king and rook are empty
        if any(board[7][i] != "." for i in range(1, 4)):
            return False

        # Check if the squares the king passes over are not under attack
        if any(is_square_attacked(board, 7, i, "black") for i in range(2, 5)):
            return False

        return True


    def black_king_side_castle_possible(board):
        # Check if the black king is in the correct starting position
        if board[0][4] != "k":
            return False

        # Check if the black king's rook is in the correct starting position
        if board[0][7] != "r":
            return False

        # Check if the squares between the king and rook are empty
        if any(board[0][i] != "." for i in range(5, 7)):
            return False

        # Check if the squares the king passes over are not under attack
        if any(is_square_attacked(board, 0, i, "white") for i in range(4, 7)):
            return False

        return True


    def black_queen_side_castle_possible(board):
        # Check if the black king is in the correct starting position
        if board[0][4] != "k":
            return False

        # Check if the black queen's rook is in the correct starting position
        if board[0][0] != "r":
            return False

        # Check if the squares between the king and rook are empty
        if any(board[0][i] != "." for i in range(1, 4)):
            return False

        # Check if the squares the king passes over are not under attack
        if any(is_square_attacked(board, 0, i, "white") for i in range(2, 5)):
            return False

        return True


    def is_square_attacked(board, row, col, attacking_side):
        # Logic to check if a square is attacked by pieces of the given side
        # Implement this based on your existing code or chess rules

        return False  # Placeholder implementation




    def board_to_fen(board):
        # Use StringIO to build string more efficiently than concatenating
        with io.StringIO() as s:
            for row in board:
                empty = 0
                for cell in row:
                    c = cell[0]
                    if c != ".":
                        if empty > 0:
                            s.write(str(empty))
                            empty = 0
                        s.write(cell[0].upper() if cell[0].isupper() else cell[0].lower())
                    else:
                        empty += 1
                if empty > 0:
                    s.write(str(empty))
                s.write('/')
            # Move one position back to overwrite last '/'
            s.seek(s.tell() - 1)
            # Add castling rights
            s.write(' w')
            
            # Check if white can castle kingside
            if white_king_side_castle_possible(board):
                s.write('K')
            
            # Check if white can castle queenside
            if white_queen_side_castle_possible(board):
                s.write('Q')
            
            # Check if black can castle kingside
            if black_king_side_castle_possible(board):
                s.write('k')
            
            # Check if black can castle queenside
            if black_queen_side_castle_possible(board):
                s.write('q')
            
            # Add the remaining FEN fields
            s.write(' - 0 1')
            return s.getvalue()


    Finding_Empty_Spaces = spaces.copy()

    for i in all_pieces:
        Finding_Empty_Spaces.remove(i[:2])

    sorted_array = sorted(all_pieces, key=lambda x: (x[1], x[0]))
    sorted_Empties = sorted(Finding_Empty_Spaces, key=lambda x: (x[1], x[0]))

    chessboard = [['.' for _ in range(8)] for _ in range(8)]

    # Place the pieces on the chessboard
    for piece in sorted_array:
        position = piece[:2]
        row = int(position[1]) - 1
        col = 7 - (ord(position[0]) - ord('a'))
        chessboard[row][col] = piece[3:]

    # Print the chessboard
    for row in chessboard:
        print(' '.join(row))

    fen = board_to_fen(chessboard)
    try:
        stockfish.set_fen_position(fen)
        print("Best Move: " + str(stockfish.get_best_move()))
        time.sleep(1)
    except:
        time.sleep(1)
