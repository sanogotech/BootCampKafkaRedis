package com.mitrais.kafka.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

import com.mitrais.persistence.entity.MUser;
import com.mitrais.persistence.service.UserDAO;
import com.mitrais.utils.JsonUtil;

@Service
public class MessageListenerImpl implements MessageListener{
	
	@Autowired
	private UserDAO dao;
	
	@Override
	@KafkaListener(topics="${kafka.my.topic}")
	public void listen(String jsonStr) throws Exception {
		MUser kafkaUser = JsonUtil.parseJson(jsonStr, MUser.class);
		/*
		MUser user = new  MUser();
		user.setId(kafkaUser.getId());
		user.setUserId(kafkaUser.getUserId());
		user.setEmail(kafkaUser.getEmail());
		user.setFullName(kafkaUser.getFullName());
		user.setPassword(kafkaUser.getPassword());
		*/
		dao.saveMUser(kafkaUser);
		System.out.println("======================> Consumed Message: "+jsonStr);
	}

}
