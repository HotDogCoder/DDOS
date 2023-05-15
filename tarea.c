#include <stdio.h>
#include <string.h>

int main() {
  char* word_list[] = {"apple", "banana", "cherry", "date", "elderberry"};
  int num_words = sizeof(word_list) / sizeof(char*);
  char input_word[50];
  int i, found = 0;
  
  printf("Enter a word: ");
  scanf("%s", input_word);
  
  for (i = 0; i < num_words; i++) {
    if (strcmp(word_list[i], input_word) == 0) {
      found = 1;
      break;
    }
  }
  
  if (found) {
    printf("%s is in the list.\n", input_word);
  } else {
    printf("Sorry, %s is not in the list.\n", input_word);
  }
  
  return 0;
}