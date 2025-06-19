function scrollToBottom() {
    var messageBody = document.getElementById("messageFormeight");
    messageBody.scrollTop = messageBody.scrollHeight;
  }
  
  $(document).ready(function () {
    $("#messageArea").on("submit", function (event) {
      const date = new Date();
      const hour = date.getHours();
      const minute = date.getMinutes();
      const str_time = `${hour % 12 || 12}:${minute < 10 ? "0" + minute : minute} ${hour >= 12 ? "PM" : "AM"}`;
      var rawText = $("#text").val();
      var userHtml =
        '<div class="d-flex justify-content-end mb-4"><div class="msg_cotainer_send">' +
        rawText +
        '<div class="msg_time_send">' +
        str_time +
        '</div></div><div class="img_cont_msg"><img src="' + 
        "{{ url_for('static', filename='images/Untitled-design.png') }}" + 
        '" class="rounded-circle user_img_msg"></div></div>';
  
      $("#text").val("");
      $("#messageFormeight").append(userHtml);
  
      scrollToBottom();
  
      $.ajax({
        data: {
          msg: rawText,
        },
        type: "POST",
        url: "/get",
      }).done(function (data) {
        var botHtml =
          '<div class="d-flex justify-content-start mb-4"><div class="img_cont_msg"><img src="' + 
          "{{ url_for('static', filename='images/icons8-chatgpt-512.png') }}" + 
          '" class="rounded-circle user_img_msg"></div><div class="msg_cotainer">' +
          data +
          '<div class="msg_time">' +
          str_time +
          "</div></div></div>";
        $("#messageFormeight").append($.parseHTML(botHtml));
        scrollToBottom();
      });
      event.preventDefault();
    });
  });
  function scrollToBottom() {
      const messageBody = document.getElementById("messageFormeight");
      messageBody.scrollTop = messageBody.scrollHeight;
    }
    
    function showTypingIndicator() {
      const typingHtml = `
        <div class="d-flex justify-content-start mb-4">
          <div class="img_cont_msg">
            <img src="https://i.ibb.co/fSNP7Rz/icons8-chatgpt-512.png" class="rounded-circle user_img_msg">
          </div>
          <div class="typing-indicator">
            <div class="typing-dot"></div>
            <div class="typing-dot" style="animation-delay: 0.2s"></div>
            <div class="typing-dot" style="animation-delay: 0.4s"></div>
          </div>
        </div>
      `;
      $("#messageFormeight").append(typingHtml);
      scrollToBottom();
    }
    
    $(document).ready(function () {
      $("#messageArea").on("submit", function (event) {
        event.preventDefault();
    
        const date = new Date();
        const hour = date.getHours();
        const minute = date.getMinutes();
        const str_time = `${hour}:${minute < 10 ? "0" + minute : minute}`;
        const rawText = $("#text").val().trim();
    
        if (!rawText) return;
    
        const userHtml = `
          <div class="d-flex justify-content-end mb-4">
            <div class="msg_cotainer_send">
              ${rawText}
              <span class="msg_time">${str_time}</span>
            </div>
            <div class="img_cont_msg">
              <img src="https://i.ibb.co/d5b84Xw/Untitled-design.png" class="rounded-circle user_img_msg">
            </div>
          </div>
        `;
    
        $("#text").val("");
        $("#messageFormeight").append(userHtml);
        scrollToBottom();
    
        showTypingIndicator();
    
        // Simulate bot response (replace with actual AJAX call)
        setTimeout(() => {
          $(".typing-indicator").last().remove();
    
          const botHtml = `
            <div class="d-flex justify-content-start mb-4">
              <div class="img_cont_msg">
                <img src="https://i.ibb.co/fSNP7Rz/icons8-chatgpt-512.png" class="rounded-circle user_img_msg">
              </div>
              <div class="msg_cotainer">
                Thank you for your message! We'll get back to you shortly.
                <span class="msg_time">${str_time}</span>
              </div>
            </div>
          `;
    
          $("#messageFormeight").append(botHtml);
          scrollToBottom();
        }, 1500);
      });
    });