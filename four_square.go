/*
description:

Four-Square Cipher algorithm
https://en.wikipedia.org/wiki/Four-square_cipher

author: Fran Raknić fraknic@tvz.hr
*/

package main

import(
	f "fmt"
	s "strings"
	rand "math/rand"
	"time"
)

func to_bigrams(str string) []string {
	
	var bigrams string

	if len(str) % 2 != 0{
		str += "x"
	}

	str = s.Replace(str, " ", "", -1)
	str = s.ToLower(str)
	
	for index, char := range str{
		if index % 2 == 0 && index != 0{
			bigrams += " "
		}

		bigrams += f.Sprintf("%c", char)			
	}

	return s.Split(bigrams, " ")
}

func generate_random_matrix() [5][5]string{

	var allowed_letters = []string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
	var random_matrix [5][5]string

	allowed_letters = shuffle(allowed_letters)

	i := 0
	j := 0

	for n := 0; n < len(allowed_letters); n++ {	
		
		random_matrix[i][j] = allowed_letters[n]
		if((n + 1) % 5 == 0 && n != 0){
			i = 0
			j += 1
		}else{
			i += 1
		}
	}

	return random_matrix
}

func shuffle(src []string) []string {
	final := make([]string, len(src))
	rand.Seed(time.Now().UnixNano())
	perm := rand.Perm(len(src))

	for i, v := range perm {
			final[v] = src[i]
	}
	return final
}

func encrypt(plaintext string, rmtx1 [5][5]string, rmtx2 [5][5]string) string{

	var cipher_text string
	mtx1 := [5][5]string{{"a","b","c","d","e"},{"f","g","h","i","k"}, {"l","m","n","o","p"}, {"q","r","s","t","u"}, {"v","w","x","y","z"}}

	bigrams := to_bigrams(plaintext)

	for _, bigram := range bigrams {

		row1, col1 := get_char_index(f.Sprintf("%c", bigram[0],), mtx1)
		row2, col2 := get_char_index(f.Sprintf("%c", bigram[1],), mtx1)

		char1 := rmtx1[row1][col1]
		char2 := rmtx2[row2][col2]

		cipher_text += char1+char2

	}

	return cipher_text
}

func decrypt(cipher_text string, rmtx1 [5][5]string, rmtx2 [5][5]string) string{
	 
	var plaintext string
	mtx1 := [5][5]string{{"a","b","c","d","e"},{"f","g","h","i","k"}, {"l","m","n","o","p"}, {"q","r","s","t","u"}, {"v","w","x","y","z"}}


	bigrams := to_bigrams(cipher_text)

	for _, bigram := range bigrams {

		row1, col1 := get_char_index(f.Sprintf("%c", bigram[0],), rmtx1)
		row2, col2 := get_char_index(f.Sprintf("%c", bigram[1],), rmtx2)

		char1 := mtx1[row1][col1]
		char2 := mtx1[row2][col2]

		plaintext += char1+char2

	}

	return plaintext
}

func get_char_index(letter string, matrix [5][5]string )(int, int){
	for r := 0; r < 5; r++ {
		for c := 0; c < 5; c++ {
			if(matrix[r][c] == letter){
				return r, c
			}
		}
	}
	return -1, -1
}

func main(){

	rmtx1 := generate_random_matrix()
	rmtx2 := generate_random_matrix()

	f.Println("Encryption matrix:")
	f.Println(rmtx1)
	f.Println(rmtx2)

	message := "attack at dawn"

	f.Println("Encrypting: ", message)

	cipher_text := encrypt(message, rmtx1, rmtx2)
	f.Println("Encrypted: ", cipher_text)

	plaintext := decrypt(cipher_text, rmtx1, rmtx2)
	f.Println("Decrypted: ", plaintext)

}