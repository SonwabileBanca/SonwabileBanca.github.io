public class OverloadingExample {
    private static final String integer = "Seven-7";
    private static final String string = "\tThirty Three-33";
    // overload function
    void overloadedfunction (int i) {
        System.out.println("In Overload parameters with-" + i);

    }
    void overloadedfunction(int x, String str) {
        System.out.println(" In overlead with parameters in-" + integer + " "  +string);
    }
    public static void main(String[] args) {
        OverloadingExample obj = new OverloadingExample();
        obj.overloadedfunction(8);
        obj.overloadedfunction(8, "Hello Overload");
    }
    
}
