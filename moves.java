/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package chessboardgui;

/**
 *
 * @author Deviare User
 */
public class moves {
    //private static final int SIZE = 8;

    public static boolean isValidMove(String piece, int startRow, int startCol, int endRow, int endCol) {
        return switch (piece.toLowerCase()) {
            case "pawn" -> isValidPawnMove(startRow, startCol, endRow, endCol);
            case "knight" -> isValidKnightMove(startRow, startCol, endRow, endCol);
            case "bishop" -> isValidBishopMove(startRow, startCol, endRow, endCol);
            case "rook" -> isValidRookMove(startRow, startCol, endRow, endCol);
            case "queen" -> isValidQueenMove(startRow, startCol, endRow, endCol);
            case "king" -> isValidKingMove(startRow, startCol, endRow, endCol);
            default -> false;
        };
    }

    private static boolean isValidPawnMove(int startRow, int startCol, int endRow, int endCol) {
        return endRow == startRow + 1 && startCol == endCol; // Basic forward move
    }

    private static boolean isValidKnightMove(int startRow, int startCol, int endRow, int endCol) {
        return (Math.abs(startRow - endRow) == 2 && Math.abs(startCol - endCol) == 1) ||
               (Math.abs(startRow - endRow) == 1 && Math.abs(startCol - endCol) == 2); // "L" shape move
    }

    private static boolean isValidBishopMove(int startRow, int startCol, int endRow, int endCol) {
        return Math.abs(startRow - endRow) == Math.abs(startCol - endCol); // Diagonal move
    }

    private static boolean isValidRookMove(int startRow, int startCol, int endRow, int endCol) {
        return (startRow == endRow || startCol == endCol); // Straight move
    }

    private static boolean isValidQueenMove(int startRow, int startCol, int endRow, int endCol) {
        return isValidBishopMove(startRow, startCol, endRow, endCol) || isValidRookMove(startRow, startCol, endRow, endCol);
    }

    private static boolean isValidKingMove(int startRow, int startCol, int endRow, int endCol) {
        return Math.abs(startRow - endRow) <= 1 && Math.abs(startCol - endCol) <= 1; // One step in any direction
    }
}