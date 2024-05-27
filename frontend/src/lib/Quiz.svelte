<script>
  export let title;
  export let questions;

  let selectedAnswers = new Array(questions.length).fill(null); // Initialize as an array with null values for each question
  let submitted = new Array(questions.length).fill(false); // Track submitted state for each question

  function handleAnswerChange(questionIndex, answerIndex) {
    if (!submitted[questionIndex]) {
      selectedAnswers[questionIndex] = answerIndex;
    }
  }

  function handleSubmit(questionIndex) {
    submitted[questionIndex] = true;
  }
</script>

<style>
  .quiz-container {
    margin-top: 20px;
  }
  .quiz-title{
      margin-top: 80px;
      margin-bottom: 20px;
      font-size: 28px;
      font-style: italic;
  }
  .question {
    margin-bottom: 20px;
    padding: 10px;
    border-radius: 5px;
  }
  .question-text{
      font-size: 18px;
      margin-bottom: 15px;
      font-weight: 600;
  }
  .answers {
      list-style-type: none;
      padding: 0;
      display: flex;
      flex-direction: column;
      gap: 20px;
  }
  .answer {
    margin-bottom: 10px;
  }
  .correct {
    background-color: #d4edda;
  }
  .incorrect {
    background-color: #f8d7da;
  }
  .btn {
    margin-top: 10px;
    padding: 10px;
    background-color: #FFDE4B;
    color: #0a0a0a;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    font-weight: 500;
    transition: .2s;
  }
  .btn:hover {
    background-color: #0a0a0a;
    color: #fff;
  }

  .question-label {
    display: flex;
    align-items: baseline;
    gap: 15px;
    font-size: 18px;
    cursor: pointer;
  }
  .correct-answer {
    font-size: 16px;
    font-weight: 600;
    color: green;
    margin-top: 10px;
  }
</style>

<div class="quiz-container">
  <h5 class="quiz-title">{title}</h5>
  {#if questions && questions.length > 0}
      {#each questions as question, questionIndex}
          <div class="question {submitted[questionIndex] ? (questions[questionIndex].answers[selectedAnswers[questionIndex]].is_correct ? 'correct' : 'incorrect') : ''}">
              <p class="question-text">{question.question_text}</p>
              <ul class="answers">
                  {#each question.answers as answer, answerIndex}
                      <li class="answer">
                          <label class="question-label">
                              <input
                                type="radio"
                                name={`question-${questionIndex}`}
                                value={answerIndex}
                                on:change={() => handleAnswerChange(questionIndex, answerIndex)}
                                disabled={submitted[questionIndex]}
                              />
                              {answer.answer_text}
                          </label>
                      </li>
                  {/each}
              </ul>
              <button class="btn" on:click={() => handleSubmit(questionIndex)} disabled={selectedAnswers[questionIndex] == null || submitted[questionIndex]}>
                  Ответить
              </button>
              {#if submitted[questionIndex] && !questions[questionIndex].answers[selectedAnswers[questionIndex]].is_correct}
                  <p class="correct-answer">
                      Правильный ответ: 
                      {#each question.answers as answer, answerIndex (answerIndex)}
                          {#if answer.is_correct}
                              {answer.answer_text}
                          {/if}
                      {/each}
                  </p>
              {/if}
          </div>
      {/each}
  {:else}
      <p>Нет вопросов для отображения.</p>
  {/if}
</div>
