package main

// import (
// 	"encoding/json"
// 	"fmt"
// 	"log"
// 	"math/rand"
// 	"net/http"
// 	"time"

// 	"github.com/gorilla/mux"
// )

// func main() {
// 	router := mux.NewRouter()
// 	router.HandleFunc("/booking", RequestBooking).Methods("POST")
// 	log.Fatal(http.ListenAndServe(":5000", router))
// }

// type BookingReq struct {
// 	Username    string `json:"username"`
// 	Destination string `json:"destination"`
// }

// type Booking struct {
// 	Code        string 	`json:"code"`
// 	Username    string	`json:"username"`
// 	Destination string	`json:"destination"`
// }

// type Response struct {
// 	Message string
// }

// func RequestBooking(w http.ResponseWriter, r *http.Request) {
// 	// Create payload bertipe BookingReq
// 	var bookingReq BookingReq
// 	// Masukkan nilai r.Body ke dalam bookingReq variable
// 	_ = json.NewDecoder(r.Body).Decode(&bookingReq)
// 	// buat code dari random String with Charset
// 	code := StringWithCharset(5, charset)

// 	booking := Booking{code, bookingReq.Username, bookingReq.Destination}

// 	sendMessage(booking)

// 	response := Response{"Booking Success, Your Booking Code : " + booking.Code}
// 	json.NewEncoder(w).Encode(response)
// }

// var seededRand *rand.Rand = rand.New(rand.NewSource(time.Now().UnixNano()))

// const charset = "abcdefghijklmnopqrstuvwxyz" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

// func StringWithCharset(length int, charset string) string {
// 	b := make([]byte, length)
// 	for i := range b {
// 		b[i] = charset[seededRand.Intn(len(charset))]
// 	}
// 	return string(b)
// }

// func failOnError(err error, msg string) {
// 	if err != nil {
// 		log.Fatalf("%s: %s", msg, err)
// 	}
// }

// // mengirim message ke Message Brocker (Publisher)
// func sendMessage(booking Booking) {
// 	conn, err := amqp.Dial("amqp://guest:guest@localhost:8083")
// 	failOnError(err, "Fail to connect to AMQP")

// 	defer conn.Close()
// 	ch, err := conn.Channel()
// 	failOnError(err, "fail to connect to Channel")

// 	defer ch.Close()

// 	q, err := ch.QueueDeclare(
// 		"Booking", // Queue name
// 		true,      // durable
// 		false,     //delete when use
// 		false,     //exclusive
// 		false,     // no-wait
// 		nil,       /// no
// 	)
// 	failOnError(err, "Fail to declare a queue")

// 	msg, err := json.Marshal(booking)

// 	if err != nil {
// 		panic(err)
// 	}

// 	err = ch.Publish(
// 		"NotifExchange", q.Name, false, false,
// 		amqp.Publishing{
// 			ContentType: "text/plain",
// 			Body:        []byte(string(msg)),
// 		},
// 	)
// 	log.Printf("[x] Sent %s", msg)
// 	failOnError(err, "Fail to publish message")
// }

// // Menerima message dari Message Brocker (Consumer)

// func ReceiveMessage() {
// 	conn, err := amqp.Dial("amqp://guest:guest@localhost:8083")
// 	failOnError(err, "Failed to connect AMQP")

// 	defer conn.Close()

// 	ch, err := conn.Channel()
// 	failOnError(err, "Fail to open channel")

// 	defer ch.Close()

// 	q, err := ch.QueueDeclare("Booking", true, false, false, false, nil) // nil == Argument
// 	failOnError(err, "Fail to declare a queue")

// 	msgs, err := ch.Consume(
// 		q.Name,
// 		"", // Consumer
// 		true,
// 		false,
// 		false,
// 		false,
// 		nil,
// 	)
// 	failOnError(err, "Failed to register a consumer")

// 	forever := make(chan bool)

// 	go func() {
// 		for d := range msgs {
// 			msg := string(d.Body)

// 			booking := Booking{}

// 			json.Unmarshal([]byte(msg), &booking)
// 			fmt.Println("Sending notification to user " + booking.Username + " with booking code " + booking.Code)
// 		}
// 	}()

// 	fmt.Println("Waiting for message, to exit press C + CTRL")
// 	<-forever
// }
