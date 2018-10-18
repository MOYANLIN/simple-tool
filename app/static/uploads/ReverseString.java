package leetcode;

import java.util.Stack;

public class ReverseString {/*
	public static void main(String[] args){
		String a =" abd asdf        asdf";
		String[] b = a.split("\\s+");
		for(int i=0;i<b.length;i++){
			System.out.println(b[i]);
		}
		String result= reverseWords(" 1");
		System.out.println(result);
	}
    public static String reverseWords(String s) {
        if(s==" ")return s;
        if(s.length()==1)return s;
        String[] a= s.split("\\s+");
        for(int i=0;i<a.length;i++){
        	System.out.println(a[i]);
        }
        if(a.length==1)return s;
        Stack<String> stack = new Stack<>();
        for(int i=0;i<a.length;i++){
        	if(a[i]!=" "){
        		stack.push(a[i]);
        		System.out.println(a[i]+"hahaha");
        	}
            
        }
        String result = "";
        result+=stack.pop();
        while(!stack.isEmpty()){
            String temp= stack.pop();
            result+=" ";
            result+=temp;
        }
        return result;
    }
*/
	public static void main(String[] args){
		String a ="      fasdfsafsa fasfas asdfasfsa     fasfasfasgfdgsdg     ";
		String b = a.trim();
		System.out.println(b);
	}
}
