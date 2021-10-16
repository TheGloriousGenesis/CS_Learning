import org.junit.Test;
import static org.junit.Assert.*;

public class TestAddingNumbers {
    @Test
    public void ReturnActualValue() {
        int[] testValues = new int[] {1, 4, 5, 6};
        int result = AddingNumbers.AddNumbers(testValues);
        assertEquals(16, result);
    }
}