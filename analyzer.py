import cv2
import numpy as np
import chess#https://github.com/niklasf/python-chess
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import numpy as np

board_img = cv2.imread('board.jpg')
empty_img = cv2.imread('empty.jpeg')

BBishop_img = cv2.imread('BlackPieces/BBishop.jpg')
BKing_img = cv2.imread('BlackPieces/BKing.jpg')
BKnight_img = cv2.imread('BlackPieces/BKnight.jpg')
BPawn_img = cv2.imread('BlackPieces/Bpawn.jpeg')
BQueen_img = cv2.imread('BlackPieces/BQueen.jpg')
BRook_img = cv2.imread('BlackPieces/BRook.jpg')

WBishop_img = cv2.imread('WhitePieces/WBishop.jpg')
WKing_img = cv2.imread('WhitePieces/WKing.jpg')
WKnight_img = cv2.imread('WhitePieces/WKnight.jpg')
WPawn_img = cv2.imread('WhitePieces/Wpawn.jpeg')
WQueen_img = cv2.imread('WhitePieces/WQueen.jpg')
WRook_img = cv2.imread('WhitePieces/WRook.jpg')
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
                print(space + " " + "Bishop")
                all_pieces.append(space + " " + "Bishop")
    # print("Black Bishops: ")
    # print(Black_bishop_locations)




    #BlackKing
    BlackKing = cv2.matchTemplate(board_img, BKing_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(BlackKing)
    yloc, xloc = np.where(BlackKing >= .8)
    Black_king_locations = []
    for (x, y) in zip(xloc, yloc):
        cv2.rectangle(board_img, (x, y), (x + 50, y + 50), (255,0,255), 2)
        Black_king_locations.append([x, y, x + 50, y + 50])
    Black_king_locations = filter_duplicates(Black_king_locations, distance_threshold)
    rect, weights = cv2.groupRectangles(Black_king_locations, 1, 0.5)
    for king in Black_king_locations:
        for space, polygon in zip(spaces, Polygons):
            if is_inside_polygon((king[0] + 25, king[1] + 25), polygon):
                print(space + " " + "King")
                all_pieces.append(space + " " + "King")
    # print("Black Kings: ")
    # print(Black_king_locations)

    #BlackKnights
    BlackKnights = cv2.matchTemplate(board_img, BKnight_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(BlackKnights)
    yloc, xloc = np.where(BlackKnights >= .8)
    Black_Knight_locations = []
    for (x, y) in zip(xloc, yloc):
        cv2.rectangle(board_img, (x, y), (x + 50, y + 50), (255,0,0), 2)
        Black_Knight_locations.append([x, y, x + 50, y + 50])
    Black_Knight_locations = filter_duplicates(Black_Knight_locations, distance_threshold)
    rect, weights = cv2.groupRectangles(Black_Knight_locations, 1, 0.5)
    for knight in Black_Knight_locations:
        for space, polygon in zip(spaces, Polygons):
            if is_inside_polygon((knight[0] + 25, knight[1] + 25), polygon):
                print(space + " " + "Knight")
                all_pieces.append(space + " " + "Knight")
    # print("Black Knights: ")
    # print(Black_Knight_locations)





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
                print(space + " " + "Pawn")
                all_pieces.append(space + " " + "Pawn")
    # print("Black Pawns: ")
    # print(Black_Pawn_locations)



    #BlackQueens
    BlackQueens = cv2.matchTemplate(board_img, BQueen_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(BlackQueens)
    yloc, xloc = np.where(BlackQueens >= .5)
    Black_Queen_locations = []
    for (x, y) in zip(xloc, yloc):
        cv2.rectangle(board_img, (x, y), (x + 50, y + 50), (100,100,100), 2)
        Black_Queen_locations.append([x, y, x + 50, y + 50])
    Black_Queen_locations = filter_duplicates(Black_Queen_locations, distance_threshold)
    rect, weights = cv2.groupRectangles(Black_Queen_locations, 1, 0.5)
    for queen in Black_Queen_locations:
        for space, polygon in zip(spaces, Polygons):
            if is_inside_polygon((queen[0] + 25, queen[1] + 25), polygon):
                print(space + " " + "Queen")
                all_pieces.append(space + " " + "Queen")
    # print("Black Queens: ")
    # print(Black_Queen_locations)



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
                print(space + " " + "Rook")
                all_pieces.append(space + " " + "Rook")
    # print("Black Rooks: ")
    # print(Black_Rook_locations)


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
    yloc, xloc = np.where(WhiteBishops >= .5)
    white_bishop_locations = []
    for (x, y) in zip(xloc, yloc):
        cv2.rectangle(board_img, (x, y), (x + 50, y + 50), (255,255,0), 2)
        white_bishop_locations.append([x, y, x + 50, y + 50])
    white_bishop_locations = filter_duplicates(white_bishop_locations, distance_threshold)
    rect, weights = cv2.groupRectangles(white_bishop_locations, 1, 0.5)
    for bishop in white_bishop_locations:
        for space, polygon in zip(spaces, Polygons):
            if is_inside_polygon((bishop[0] + 25, bishop[1] + 25), polygon):
                print(space + " " + "Bishop")
                all_pieces.append(space + " " + "Bishop")
    # print("White Bishops: ")
    # print(white_bishop_locations)

    #WhiteKing
    WhiteKing = cv2.matchTemplate(board_img, WKing_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(WhiteKing)
    yloc, xloc = np.where(WhiteKing >= .5)
    white_king_locations = []
    for (x, y) in zip(xloc, yloc):
        cv2.rectangle(board_img, (x, y), (x + 50, y + 50), (255,0,255), 2)
        white_king_locations.append([x, y, x + 50, y + 50])
    white_king_locations = filter_duplicates(white_king_locations, distance_threshold)
    rect, weights = cv2.groupRectangles(white_king_locations, 1, 0.5)
    for king in white_king_locations:
        for space, polygon in zip(spaces, Polygons):
            if is_inside_polygon((king[0] + 25, king[1] + 25), polygon):
                print(space + " " + "King")
                all_pieces.append(space + " " + "King")
    # print("White Kings: ")
    # print(white_king_locations)

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
                print(space + " " + "Knight")
                all_pieces.append(space + " " + "Knight")
    # print("White Knights: ")
    # print(white_knight_locations)

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
                print(space + " " + "Pawn")
                all_pieces.append(space + " " + "Pawn")
    # print("White Pawns: ")
    # print(white_pawn_locations)

    #WhiteQueens
    WhiteQueens = cv2.matchTemplate(board_img, WQueen_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(WhiteQueens)
    yloc, xloc = np.where(WhiteQueens >= .5)
    white_queen_locations = []
    for (x, y) in zip(xloc, yloc):
        cv2.rectangle(board_img, (x, y), (x + 50, y + 50), (0,255,0), 2)
        white_queen_locations.append([x, y, x + 50, y + 50])
    white_queen_locations = filter_duplicates(white_queen_locations, distance_threshold)
    rect, weights = cv2.groupRectangles(white_queen_locations, 1, 0.5)
    for queen in white_queen_locations:
        for space, polygon in zip(spaces, Polygons):
            if is_inside_polygon((queen[0] + 25, queen[1] + 25), polygon):
                print(space + " " + "Queen")
                all_pieces.append(space + " " + "Queen")
    # print("White Queens: ")
    # print(white_queen_locations)

    #WhiteRooks
    WhiteRooks = cv2.matchTemplate(board_img, WRook_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(WhiteRooks)
    yloc, xloc = np.where(WhiteRooks >= .5)
    white_rook_locations = []
    for (x, y) in zip(xloc, yloc):
        cv2.rectangle(board_img, (x, y), (x + 50, y + 50), (0,0,0), 2)
        white_rook_locations.append([x, y, x + 50, y + 50])
    white_rook_locations = filter_duplicates(white_rook_locations, distance_threshold)
    rect, weights = cv2.groupRectangles(white_rook_locations, 1, 0.5)
    for rook in white_rook_locations:
        for space, polygon in zip(spaces, Polygons):
            if is_inside_polygon((rook[0] + 25, rook[1] + 25), polygon):
                print(space + " " + "Rook")
                all_pieces.append(space + " " + "Rook")
    # print("White Rooks: ")
    # print(white_rook_locations)



cv2.imshow('Board', board_img)
cv2.waitKey()
cv2.destroyAllWindows()
all_pieces.sort()
print(all_pieces)
