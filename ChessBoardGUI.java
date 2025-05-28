/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package chessboardgui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;

public class ChessBoardGUI {
    private static final int SIZE = 8;
    private final JFrame frame;
    private final JButton[][] boardSquares = new JButton[SIZE][SIZE];
    private int selectedRow = -1, selectedCol = -1;
    private String selectedPiece = "";

    public ChessBoardGUI() {
        frame = new JFrame("Chessboard");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 600);
        frame.setLayout(new GridLayout(SIZE, SIZE));

        initializeBoard();
        frame.setVisible(true);
    }

    private void initializeBoard() {
        for (int row = 0; row < SIZE; row++) {
            for (int col = 0; col < SIZE; col++) {
                JButton button = new JButton();
                button.setBackground((row + col) % 2 == 0 ? Color.WHITE : Color.BLACK);
                boardSquares[row][col] = button;

                // Add Click Listener
                button.addActionListener((ActionEvent e) -> {
                    handleMove(button);
                });

                frame.add(button);
            }
        }

        placePieces();
    }

    private void handleMove(JButton button) {
        for (int row = 0; row < SIZE; row++) {
            for (int col = 0; col < SIZE; col++) {
                if (boardSquares[row][col] == button) {
                    if (selectedPiece.isEmpty()) {
                        // Select the piece
                        selectedRow = row;
                        selectedCol = col;
                        selectedPiece = getPieceName(row, col);
                        System.out.println("Selected piece: " + selectedPiece);
                    } else {
                        // Validate and move the piece
                        if (moves.isValidMove(selectedPiece, selectedRow, selectedCol, row, col)) {
                            boardSquares[row][col].setIcon(boardSquares[selectedRow][selectedCol].getIcon());
                            boardSquares[selectedRow][selectedCol].setIcon(null);
                            selectedPiece = "";
                        } else {
                            System.out.println("Invalid move!");
                        }
                    }
                    return;
                }
            }
        }
    }

    private void placePieces() {
        placePiece("pawn", 6, "/chessboardgui/pieces/w-pawn.png");
        placePiece("pawn", 1, "/chessboardgui/pieces/b-pawn.png");
        placePiece("rook", 7, "/chessboardgui/pieces/w-rook.png");
        placePiece("rook", 0, "/chessboardgui/pieces/b-rook.png");
        placePiece("knight", 7, "/chessboardgui/pieces/w-knight.png");
        placePiece("knight", 0, "/chessboardgui/pieces/b-knight.png");
        placePiece("bishop", 7, "/chessboardgui/pieces/w-bishop.png");
        placePiece("bishop", 0, "/chessboardgui/pieces/b-bishop.png");
        placePiece("queen", 7, "/chessboardgui/pieces/w-queen.png");
        placePiece("queen", 0, "/chessboardgui/pieces/b-queen.png");
        placePiece("king", 7, "/chessboardgui/pieces/w-king.png");
        placePiece("king", 0, "/chessboardgui/pieces/b-king.png");
    }

    private void placePiece(String piece, int row, String imagePath) {
        ImageIcon icon = new ImageIcon(getClass().getResource(imagePath));
        if (icon.getImage() == null) {
            System.out.println("Error loading image: " + imagePath);
            return;
        }

        for (int col = 0; col < SIZE; col++) {
            if (piece.equals("pawn") && (row == 1 || row == 6)) {
                boardSquares[row][col].setIcon(icon);
            } else if (piece.equals("rook") && (col == 0 || col == 7)) {
                boardSquares[row][col].setIcon(icon);
            } else if (piece.equals("knight") && (col == 1 || col == 6)) {
                boardSquares[row][col].setIcon(icon);
            } else if (piece.equals("bishop") && (col == 2 || col == 5)) {
                boardSquares[row][col].setIcon(icon);
            } else if (piece.equals("queen") && col == 3) {
                boardSquares[row][col].setIcon(icon);
            } else if (piece.equals("king") && col == 4) {
                boardSquares[row][col].setIcon(icon);
            }
        }
    }

    private String getPieceName(int row, int col) {
        ImageIcon icon = (ImageIcon) boardSquares[row][col].getIcon();
        if (icon == null) return "";

        String path = icon.getDescription();
        if (path.contains("pawn")) return "pawn";
        if (path.contains("rook")) return "rook";
        if (path.contains("knight")) return "knight";
        if (path.contains("bishop")) return "bishop";
        if (path.contains("queen")) return "queen";
        if (path.contains("king")) return "king";
        return "";
    }

    public static void main(String[] args) {
        ChessBoardGUI start = new ChessBoardGUI();
    }
}