import java.util.Arrays;
public class Ere{

public static int[] even(int[][] number){

int niug=0; 
b  
for(int count = 0; count < number.length; count++){
if (number[count] %2 == 0){
niug++;
}
}

int[] outpu = new int[niug];
int yssg=0;
for(int count = 0; count < number.length; count++){ 
if (number[count] %2 == 0){
outpu[yssg] = number[count];
yssg++;
}
}
return outpu;
}

public static void main(String...args){
int[] number = {1, 2, 3, 4, 5, 6};
System.out.print(Arrays.toString(even(number)));

}
}



